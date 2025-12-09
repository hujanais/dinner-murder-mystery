"""
Pydantic models for Guest and Detective entities.
"""

from ast import Dict
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from server.models.conversation import ConversationItem

class Gender(str, Enum):
    """Gender types."""
    MALE = "Male"
    FEMALE = "Female"


class Guest(BaseModel):
    """
    Pydantic model for Guest character.
    """
    name: str = Field(..., description="Name of the guest")
    age: int = Field(..., gt=0, description="Age of the guest")
    demeanor: Dict[str, str] = Field(..., description="Guest's demeanor type")
    backstory: str = Field(..., description="Knowledge base including potential motives")
    is_criminal: bool = Field(default=False, description="Boolean flag indicating if this guest is the criminal")
    gender: Gender = Field(..., description="Gender of the guest")

    def respond(self, question: str) -> str:
        """
        Respond to a question.
        """
        # respond to the question based on the guest's demeanor and backstory
        pass

    def interject(self, conversation: list[ConversationItem]) -> str:
        """
        Interject to a question that was directed to another guest.
        """
        # interject to the question based on the guest's demeanor and backstory
        pass

    class Config:
        from_attributes = True
        use_enum_values = True


class Detective(BaseModel):
    """
    Pydantic model for Detective (Player).
    Inherits from Guest with is_criminal = False.
    """
    name: str = Field(..., description="Name of the detective")
    age: int = Field(..., gt=0, description="Age of the detective")
    backstory: str = Field(..., description="Detective's background")
    gender: Gender = Field(..., description="Gender of the detective")

    class Config:
        from_attributes = True
        use_enum_values = True