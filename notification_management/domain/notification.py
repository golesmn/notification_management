from shared.abstractions.primitives.aggregate import AggregateRoot


class Notification(AggregateRoot):
    def __init__(self, id: str, title: str, type: str):
        super().__init__()
        self.id= id
        self.title = title
        self.type = type

    @classmethod
    def create(cls, id: str, title: str, type: str):
        instance = cls(id, title, type)
        return instance
    
    

    