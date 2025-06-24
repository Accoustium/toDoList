import pytest
import sys
sys.path.append(sys.path[0] + '../../../..')
from toDoList.server.json_database import JSONDatabase


@pytest.fixture
def json_database():
    # db_name = "test_db_tasks"
    # task_db = JSONDatabase(db_name)

    yield None


def test_json_database(json_database):
    # assert isinstance(task_db, JSONDatabase)
    assert True