import os
from typing import Any
import sys
sys.path.append(os.path.dirname(sys.path[0]) + '/..')
import pygrpc


class Database:
    db_name: str
    connection: Any

    def __init__(self, db_name, connection=None):
        self.db_name = db_name
        self.connection = connection
        self.tasks = []

    def add_task(self, task: pygrpc.ToDoItem):
        raise NotImplementedError("This method should be overridden in subclasses")

    def get_tasks(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def update_task(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def delete_task(self, task: pygrpc.ToDoItem):
        raise NotImplementedError("This method should be overridden in subclasses")

    def get_user(self, user_id: pygrpc.User.userId):
        raise NotImplementedError("This method should be overridden in subclasses")

    def update_user(self, user: pygrpc.User):
        raise NotImplementedError("This method should be overridden in subclasses")

    def get_all_users(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def update_group(self, group: pygrpc.Group):
        raise NotImplementedError("This method should be overridden in subclasses")

    def update_contact_info(self, contact_info: pygrpc.ContactInfo):
        raise NotImplementedError("This method should be overridden in subclasses")

    def update_address_info(self, address_info: pygrpc.AddressInfo):
        raise NotImplementedError("This method should be overridden in subclasses")
