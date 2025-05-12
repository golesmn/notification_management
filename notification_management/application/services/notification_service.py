from notification_management.domain.notification import Notification
from notification_management.infrastructure.models import NotificationModel
from notification_management.infrastructure.repositories.notification_repository import NotificationRepository


class NotificationService:
    def __init__(self, notification_repo: NotificationRepository):
        self.notification_repo = notification_repo
        
    def send_notification(self, notification_input: Notification):
        print("Sending Notification")
        notification = NotificationModel.from_entity(notification_input)
        self.notification_repo.save(notification)


