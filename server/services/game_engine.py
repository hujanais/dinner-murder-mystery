"""
Entrypoint for main service and game orchestration.
"""

from models.story import Story
from models.game_state import GameState


class GameEngine:
    """The game engine."""

    def __init__(self):
        self.story: Story = Story()
        # For now, we ignore the story_path argument and seed inline data.
        self.story.load_story("story.json")
        self.state: GameState = GameState()

