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


def create_agent(
    name: str,
    gender: Gender,
    age: int,
    demeanor: Deameanor,
    knowledge_base: str,
    is_criminal: bool,
) -> Agent:
    """
    Create an agent with guardrails for the mystery.
    """
    return Agent(
        name=name,
        model=openai_model,
        reasoning=True,
        description=f"""
        You role-play as {name}, a {age}-year-old {gender} in a murder mystery dinner.
        Stay strictly in character. Use your demeanor: {demeanor.description}.
        Base every answer ONLY on your knowledge base: {knowledge_base}.
        Never reveal information you do not know.
        If you are the killer ({'yes' if is_criminal else 'no'}), never confess; deflect subtly and protect yourself.
        If you are not the killer, share only what you know first-hand; avoid wild speculation.
        Keep responses concise, human, and situational.
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
        self.agent = create_agent(name, gender, age, demeanor, description, is_criminal)

    def respond(self, question: str) -> str:
        """
        Respond to a question based on the guest's demeanor and backstory.
        """
        return self.agent.print_response(question)

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
