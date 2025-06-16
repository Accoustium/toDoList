from server.json_database import JSONDatabase
from server.grpc_server import ToDoService


if __name__ == '__main__':
    user_db = JSONDatabase('user_db.json')  # Initialize your database
    task_db = JSONDatabase('todo_db.json')  # Initialize your user database
    ToDoService.serve(user_db, task_db, port=50051)