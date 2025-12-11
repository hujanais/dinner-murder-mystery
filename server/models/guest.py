"""
Pydantic models for Guest and Detective entities.
"""

from typing import Dict
from agno.agent import Agent
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from models.conversation import ConversationItem


class Gender(str, Enum):
    """Gender types."""

    MALE = "Male"
    FEMALE = "Female"


class Deameanor:
    """Describes the demeanor"""

    name: str
    description: str


class Guest:
    """
    Pydantic model for Guest character.
    """

    name: str
    age: int
    demeanor: Deameanor
    description: str
    is_criminal: bool
    gender: Gender
    url: str
    agent: Optional[Agent] = None

    def __init__(
        self,
        name: str,
        age: int,
        gender: Gender,
        description: str,
        is_criminal: bool,
        url: str,
        agent: Agent,
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.description = description
        self.is_criminal = is_criminal
        self.url = url
        self.agent = agent

    def register_agent(self, agent: Agent) -> None:
        self.agent = agent

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
