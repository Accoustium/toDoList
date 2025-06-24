from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("username", "contact", "userId")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    username: str
    contact: ContactInfo
    userId: int
    def __init__(self, username: _Optional[str] = ..., contact: _Optional[_Union[ContactInfo, _Mapping]] = ..., userId: _Optional[int] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("groupName", "members", "groupId")
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    groupName: str
    members: _containers.RepeatedCompositeFieldContainer[User]
    groupId: int
    def __init__(self, groupName: _Optional[str] = ..., members: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., groupId: _Optional[int] = ...) -> None: ...

class ContactInfo(_message.Message):
    __slots__ = ("email", "homePhone", "mobilePhone", "address", "contactId")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HOMEPHONE_FIELD_NUMBER: _ClassVar[int]
    MOBILEPHONE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTACTID_FIELD_NUMBER: _ClassVar[int]
    email: str
    homePhone: int
    mobilePhone: int
    address: AddressInfo
    contactId: int
    def __init__(self, email: _Optional[str] = ..., homePhone: _Optional[int] = ..., mobilePhone: _Optional[int] = ..., address: _Optional[_Union[AddressInfo, _Mapping]] = ..., contactId: _Optional[int] = ...) -> None: ...

class AddressInfo(_message.Message):
    __slots__ = ("addressUS", "useAddressUS", "addressId")
    ADDRESSUS_FIELD_NUMBER: _ClassVar[int]
    USEADDRESSUS_FIELD_NUMBER: _ClassVar[int]
    ADDRESSID_FIELD_NUMBER: _ClassVar[int]
    addressUS: AddressInfoUS
    useAddressUS: bool
    addressId: int
    def __init__(self, addressUS: _Optional[_Union[AddressInfoUS, _Mapping]] = ..., useAddressUS: bool = ..., addressId: _Optional[int] = ...) -> None: ...

class AddressInfoUS(_message.Message):
    __slots__ = ("Street1", "Street2", "City", "State", "Zip", "addressUSId")
    STREET1_FIELD_NUMBER: _ClassVar[int]
    STREET2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    ADDRESSUSID_FIELD_NUMBER: _ClassVar[int]
    Street1: str
    Street2: str
    City: str
    State: str
    Zip: int
    addressUSId: int
    def __init__(self, Street1: _Optional[str] = ..., Street2: _Optional[str] = ..., City: _Optional[str] = ..., State: _Optional[str] = ..., Zip: _Optional[int] = ..., addressUSId: _Optional[int] = ...) -> None: ...
