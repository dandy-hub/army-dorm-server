from typing import List, Optional

from sqlmodel import Field, SQLModel, Relationship

from dormtypes.soldier_types import DormGender
from models.users import User


class Room(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: Optional[str]
    capacity: int = Field(ge=1)
    soldiers: List[User] = Relationship(back_populates="room")
    dorm_id: int = Field(foreign_key=True)
    dormitory: "Dormitory" = Relationship(back_populates="rooms")


class Dormitory(SQLModel, table=True):
    gender: DormGender
    rooms: List[Room] = Relationship(back_populates="dorm")

