import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pygrpc import *
from concurrent import futures
import grpc
from .database import Database
from typing import List


class ToDoService(ToDoServiceServicer):
    def __init__(self, user_db: Database, task_db: Database):
        super().__init__()
        self.task_db = task_db
        self.user_db = user_db

    def CreateToDoItem(self, request: ToDoItem, context) -> ToDoId:
        item_id = self.db.create_todo_item(request)
        return ToDoId(id=item_id)

    def GetToDoItem(self, request: ToDoId, context) -> ToDoItem:
        item = self.db.get_todo_item(request.id)
        if not item:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('ToDo item not found')
            return ToDoItem()
        return item

    def UpdateToDoItem(self, request: ToDoItem, context) -> ToDoId:
        updated_id = self.db.update_todo_item(request)
        return ToDoId(id=updated_id)

    def DeleteToDoItem(self, request: ToDoId, context) -> None:
        self.db.delete_todo_item(request.id)
        return None

    def ListToDoItems(self, request, context) -> List:
        return self.db.list_todo_items()

    @classmethod
    def serve(cls, user_db: Database, task_db: Database, port: int = 50051):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_ToDoServiceServicer_to_server(ToDoService(user_db, task_db), server)
        server.add_insecure_port(f'[::]:{port}')
        server.start()
        print(f'Server started on port {port}')
        try:
            server.wait_for_termination()
        except KeyboardInterrupt:
            server.stop(0)
            print('Server stopped')
