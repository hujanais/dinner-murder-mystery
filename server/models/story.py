from agno.agent import Agent
from models.entity import Clue, Room, Solution
from models.guest import Gender, Guest
from agno.models.openai import OpenAIChat

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai_model = OpenAIChat(id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))


def create_agent(name: str) -> Agent:
    """
    Create an agent.
    """
    return Agent(
        name=name,
        model=openai_model,
        reasoning=True,
    )


class Story:
    """
    Story for the game.
    """

    def __init__(self):
        self.title: str
        self.description: str
        self.url: str
        self.story: str
        self.solution: Solution
        self.clues: list[Clue]
        self.rooms: list[Room]
        self.guests: list[Guest]

    def load_story(self, story_path: str):
        """
        Load a story from a file.
        """
        self.title = "Title of the story"
        self.description = "Description of the story"
        self.url = "URL of the story"
        self.story = "Story of the story"
        self.solution = Solution(
            title="Solution of the story",
            description="Description of the solution",
            url="URL of the solution",
        )
        self.clues = [
            Clue(
                title="Clue 1",
                description="Description of the clue 1",
                url="URL of the clue 1",
            ),
            Clue(
                title="Clue 2",
                description="Description of the clue 2",
                url="URL of the clue 2",
            ),
        ]
        self.rooms = [
            Room(
                title="Room 1",
                description="Description of the room 1",
                url="URL of the room 1",
            ),
            Room(
                title="Room 2",
                description="Description of the room 2",
                url="URL of the room 2",
            ),
        ]
        self.guests = [
            Guest(
                name="Guest 1",
                gender=Gender.MALE,
                age=30,
                description="Description of the guest 1",
                is_criminal=False,
                url="URL of the guest 1",
                agent=None,
            ),
            Guest(
                name="Guest 2",
                gender=Gender.FEMALE,
                age=25,
                description="Description of the guest 2",
                is_criminal=True,
                url="URL of the guest 2",
                agent=None,
            ),
        ]

    def save_story(self, story_path: str):
        """
        Save the story to a file.
        """
        pass
