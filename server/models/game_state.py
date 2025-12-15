from pydantic import BaseModel
from typing import Dict, List, Optional, Set

from models.conversation import ConversationItem


class GameState(BaseModel):
    """
    Per-session mutable game state.
    Tracks discovered clues, searched rooms, questions asked, and conversation history.
    """

    discovered_clue_ids: Set[str] = set()
    searched_room_ids: Set[str] = set()
    questions_asked: Dict[str, int] = {}
    conversation_log: List[ConversationItem] = []
    accused: Optional[str] = None
    game_over: bool = False

