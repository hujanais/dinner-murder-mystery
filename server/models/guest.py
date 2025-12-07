"""
Pydantic models for Guest and Detective entities.
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Demeanor(str, Enum):
    """Guest demeanor types."""
    SHY = "Shy"
    BRASH = "Brash"
    TALKATIVE = "Talkative"
    # TODO: Add more demeanor types as needed


class Gender(str, Enum):
    """Gender types."""
    MALE = "Male"
    FEMALE = "Female"


class Guest(BaseModel):
    """
    Pydantic model for Guest character.
    """
    id: Optional[int] = None
    name: str = Field(..., description="Name of the guest")
    age: int = Field(..., gt=0, description="Age of the guest")
    demeanor: Demeanor = Field(..., description="Guest's demeanor type")
    backstory: str = Field(..., description="Knowledge base including potential motives")
    is_criminal: bool = Field(default=False, description="Boolean flag indicating if this guest is the criminal")
    gender: Gender = Field(..., description="Gender of the guest")

    class Config:
        from_attributes = True
        use_enum_values = True


class Detective(BaseModel):
    """
    Pydantic model for Detective (Player).
    Inherits from Guest with is_criminal = False.
    """
    id: Optional[int] = None
    name: str = Field(..., description="Name of the detective")
    age: int = Field(..., gt=0, description="Age of the detective")
    demeanor: Demeanor = Field(..., description="Detective's demeanor type")
    backstory: str = Field(..., description="Detective's background")
    gender: Gender = Field(..., description="Gender of the detective")
    # is_criminal is always False for detectives, so it's not included

    class Config:
        from_attributes = True
        use_enum_values = True

