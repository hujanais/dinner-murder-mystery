"""
Pydantic models for EntityBase and its extensions (Room, Clue, Story, Solution).
"""

from pydantic import BaseModel, Field
from typing import Optional


class EntityBase(BaseModel):
    """
    Base Pydantic model for entities like Room, Clue, Story, Solution.
    """
    id: Optional[int] = None
    title: str = Field(..., description="Title of the entity")
    description: str = Field(..., description="Description of the entity")
    url: Optional[str] = Field(None, description="URL to an external image or HTML for display")

    class Config:
        from_attributes = True


class Room(EntityBase):
    """
    Pydantic model for Room/Location entities.
    Extends EntityBase.
    """
    pass


class Clue(EntityBase):
    """
    Pydantic model for Clue entities.
    Extends EntityBase.
    """
    room_id: Optional[int] = Field(None, description="ID of the room where this clue can be found")


class Story(EntityBase):
    """
    Pydantic model for Story entities.
    Extends EntityBase.
    """
    pass


class Solution(EntityBase):
    """
    Pydantic model for Solution entities.
    Extends EntityBase.
    """
    pass

