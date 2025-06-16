import user_pb2 as _user_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToDoItem(_message.Message):
    __slots__ = ("author", "title", "description", "completed", "groups", "project", "priority", "dueDate", "createdAt", "updatedAt", "id", "storyPoints")
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DUEDATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STORYPOINTS_FIELD_NUMBER: _ClassVar[int]
    author: str
    title: str
    description: str
    completed: bool
    groups: _containers.RepeatedCompositeFieldContainer[_user_pb2.Group]
    project: ToDoProject
    priority: int
    dueDate: int
    createdAt: int
    updatedAt: int
    id: ToDoId
    storyPoints: int
    def __init__(self, author: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., completed: bool = ..., groups: _Optional[_Iterable[_Union[_user_pb2.Group, _Mapping]]] = ..., project: _Optional[_Union[ToDoProject, _Mapping]] = ..., priority: _Optional[int] = ..., dueDate: _Optional[int] = ..., createdAt: _Optional[int] = ..., updatedAt: _Optional[int] = ..., id: _Optional[_Union[ToDoId, _Mapping]] = ..., storyPoints: _Optional[int] = ...) -> None: ...

class ToDoProject(_message.Message):
    __slots__ = ("projectName", "projectDescription", "startDate", "endDate")
    PROJECTNAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STARTDATE_FIELD_NUMBER: _ClassVar[int]
    ENDDATE_FIELD_NUMBER: _ClassVar[int]
    projectName: str
    projectDescription: str
    startDate: int
    endDate: int
    def __init__(self, projectName: _Optional[str] = ..., projectDescription: _Optional[str] = ..., startDate: _Optional[int] = ..., endDate: _Optional[int] = ...) -> None: ...

class ToDoId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
