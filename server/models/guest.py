"""
Pydantic models for Guest and Detective entities.
"""
import os
from models.conversation import ConversationItem

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from pydantic import BaseModel, Field
from enum import Enum

from dotenv import load_dotenv
load_dotenv()

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai_model = OpenAIChat(id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))



class Gender(str, Enum):
    """Gender types."""

    MALE = "Male"
    FEMALE = "Female"


class Deameanor:
    """Describes the demeanor"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


def create_agent(name: str, gender: Gender, age: int, demeanor: Deameanor, knowledge_base: str) -> Agent:
    """
    Create an agent.
    """
    return Agent(
        name=name,
        model=openai_model,
        reasoning=True,
        description=f"""
         When you are asked a question, you should respond based on your backstory and knowledge base only.
         You should not reveal any information that is not in your knowledge base.  You are to role-play the character
         to make it as realistic as possible.
         Be playful and engaging in your responses but keep it realistic.
         You are role playing as {name} in a murder mystery game.  You are a {age} year old {gender}.
         Your demeanor is: {demeanor.description}.
         Your knowledge base is: {knowledge_base}.
        """,
    )

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

    def __init__(
        self,
        name: str,
        age: int,
        gender: Gender,
        description: str,
        is_criminal: bool,
        url: str,
        demeanor: Deameanor,
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.description = description
        self.is_criminal = is_criminal
        self.url = url
        self.demeanor = demeanor
        self.agent = create_agent(name, gender, age, demeanor, description)

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
