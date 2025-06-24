import os
from database import Database
import json
import sys
sys.path.append(os.path.dirname(sys.path[0]) + '/..')
import pygrpc


class JSONDatabase:
    def __init__(self, db_name):
        super().__init__(db_name)

    def __enter__(self):
        self.load_tasks()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")

        self.save_tasks()
        self.tasks = []

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
        result = False
        self.tasks.append(task)

        return result

    def get_tasks(self):
        result = self.tasks

        return result

    def delete_task(self, task: pygrpc.ToDoItem):
        idx = self.tasks.index(task)
        self.tasks.pop(idx)
