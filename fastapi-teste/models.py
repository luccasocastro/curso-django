from uuid import UUID, uuid4
from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male="male"
    female="female"

class Roles(str, Enum):
    user="user"
    admin="admin"
    student="student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Roles]

class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Roles]]
