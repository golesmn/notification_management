from notification_management.infrastructure.models import NotificationModel
from shared.infrastructure.db.sqlalchemy_repository import SQLAlchemyRepository
from sqlalchemy.orm import Session

class NotificationRepository(SQLAlchemyRepository[NotificationModel]):
    def __init__(self, session: Session):
        super().__init__(session, NotificationModel)
        
    