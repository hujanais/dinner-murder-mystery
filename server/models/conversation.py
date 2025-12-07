from pydantic import BaseModel

class ConversationItem(BaseModel):
    """Description of the conversation item."""
    name: str
    content: str
    url: str

class ConversationHistory():
    """Contains the list of all conversation items."""
    items: list[ConversationItem]

    def add_item(self, item: ConversationItem):
        """Add a new conversation item."""
        self.items.append(item)

    def get_items(self):
        """Get all conversation items."""
        return self.items

    def get_item(self, index: int):
        """Get a conversation item by index."""
        return self.items[index]
