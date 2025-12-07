from server.models.entity import Clue, Room, Solution
from server.models.guest import Guest

class Story():
    """
    Story for the game.
    """
    title: str
    description: str
    url: str
    story: str
    solution: Solution
    clues: list[Clue]
    rooms: list[Room]
    guests: list[Guest]

    def load_story(self, story_path: str):
        """
        Load a story from a file.
        """
        self.title = "Title of the story"
        self.description = "Description of the story"
        self.url = "URL of the story"
        self.story = "Story of the story"
        self.solution = Solution(title="Solution of the story", description="Description of the solution", url="URL of the solution")
        self.clues = [Clue(title="Clue 1", description="Description of the clue 1", url="URL of the clue 1"), Clue(title="Clue 2", description="Description of the clue 2", url="URL of the clue 2")]
        self.rooms = [Room(title="Room 1", description="Description of the room 1", url="URL of the room 1"), Room(title="Room 2", description="Description of the room 2", url="URL of the room 2")]
        self.guests = [Guest(title="Guest 1", description="Description of the guest 1", url="URL of the guest 1"), Guest(title="Guest 2", description="Description of the guest 2", url="URL of the guest 2")]


    def save_story(self, story_path: str):
        """
        Save the story to a file.
        """
        pass
