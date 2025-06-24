import sys
sys.path.append(sys.path[0] + '/..')
import pygrpc
from concurrent import futures
import grpc
from .database import Database
from typing import List


class ToDoService(pygrpc.ToDoServiceServicer):
    def __init__(self, user_db: Database, task_db: Database):
        super().__init__()
        self.task_db = task_db
        self.user_db = user_db

    def CreateToDoItem(self, request: pygrpc.ToDoItem, context) -> pygrpc.ToDoId:
        item_id = self.db.create_todo_item(request)
        return pygrpc.ToDoId(id=item_id)

    def GetToDoItem(self, request: pygrpc.ToDoId, context) -> pygrpc.ToDoItem:
        item = self.db.get_todo_item(request.id)
        if not item:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('ToDo item not found')
            return pygrpc.ToDoItem()
        return item

    def UpdateToDoItem(self, request: pygrpc.ToDoItem, context) -> pygrpc.ToDoId:
        updated_id = self.db.update_todo_item(request)
        return pygrpc.ToDoId(id=updated_id)

    def DeleteToDoItem(self, request: pygrpc.ToDoId, context) -> None:
        self.db.delete_todo_item(request.id)
        return None

    def ListToDoItems(self, request, context) -> List:
        return self.db.list_todo_items()

    @classmethod
    def serve(cls, user_db: Database, task_db: Database, port: int = 50051):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pygrpc.add_ToDoServiceServicer_to_server(ToDoService(user_db, task_db), server)
        server.add_insecure_port(f'[::]:{port}')
        server.start()
        print(f'Server started on port {port}')
        try:
            server.wait_for_termination()
        except KeyboardInterrupt:
            server.stop(0)
            print('Server stopped')
