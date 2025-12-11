"""
Entrypoint for main service
"""

from models.story import Story


class GameEngine:
    """The game engine."""

    story: Story = Story()
    story.load_story("story.json")

    def __init__(self):
        pass
