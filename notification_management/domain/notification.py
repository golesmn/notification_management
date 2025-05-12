from typing import Optional
from shared.abstractions.primitives.aggregate import AggregateRoot


class Notification(AggregateRoot):
    def __init__(self, id: Optional[str], title: str, type: str):
        super().__init__()
        self.id = id
        self.title = title
        self.type = type

    @classmethod
    def create(cls, title: str, type: str):
        instance = cls(id=100, title=title, type=type)
        return instance
    
    

    