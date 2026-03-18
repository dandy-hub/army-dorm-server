import datetime
from typing import List, Optional

from sqlmodel import Field, SQLModel, Relationship
from uuid6 import UUID,uuid7

from app_types.dorm_types import DormGender
from models.users import User


class Room(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid6.uuid7,index=True)
    name: Optional[str]
    capacity: int = Field(ge=1)
    soldiers: List[User] = Relationship(back_populates="room")
    dorm_id: int = Field(foreign_key=True)
    dormitory: "Dormitory" = Relationship(back_populates="rooms")


class Dormitory(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid7, index=True)
    name: str
    gender: DormGender
    rooms: List[Room] = Relationship(back_populates="dorm")
    base_id: int = Field(foreign_key=True)
    base: "Base" = Relationship(back_populates="dorms")


class Base(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid7, index=True)
    name: str
    dorms: List[Dormitory] = Relationship(back_populates="base")
