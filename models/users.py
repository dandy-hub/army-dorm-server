import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from uuid6 import UUID,uuid7

from app_types.soldier_types import PhoneNumber, Rank, PermissionLevel
from models.dorms import Room


class User(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid7, index=True)
    first_name: str
    last_name: str
    phone_number: PhoneNumber
    rank: Rank
    unit_name: str
    occupation: str
    permissions_level: PermissionLevel
    room_id: Optional[int] = Field(default=None, foreign_key=True, nullable=True)
    rooms: Optional[Room] = Relationship(back_populates="soldiers")
