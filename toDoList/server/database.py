from typing import Any


class Database:
    db_name: str
    connection: Any

    def __init__(self, db_name, connection=None):
        self.db_name = db_name
        self.connection = connection

    def add_task(self, task):
        raise NotImplementedError("This method should be overridden in subclasses")

    def get_tasks(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def delete_task(self, task):
        raise NotImplementedError("This method should be overridden in subclasses")
