from .database import Database
import json
import sys
sys.path.append(sys.path[0] + '/..')
import pygrpc


class JSONDatabase(Database):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.db_name, 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.db_name, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task: pygrpc.ToDoItem):
        result = super().add_task(task)
        self.save_tasks()
        return result

    def delete_task(self, task: pygrpc.ToDoItem):
        result = super().delete_task(task)
        self.save_tasks()
        return result

    def get_tasks(self):
        return super().get_tasks()
