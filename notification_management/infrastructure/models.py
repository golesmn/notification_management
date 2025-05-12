from notification_management.domain.notification import Notification
from shared.infrastructure.db.db import Base
from sqlalchemy import Column, Integer, String




class NotificationModel(Base):
    __tablename__ = "notifications"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)

    @staticmethod
    def from_entity(notification: Notification):
        return NotificationModel(
            id=notification.id, title=notification.title, type=notification.type
        )

    def to_entity(self):
        return Notification(id=self.id, title=self.title, type=self.type)
