from flask import request

from notification_management.application.services.notification_service import NotificationService
from notification_management.domain.notification import Notification
from notification_management.infrastructure.repositories.notification_repository import NotificationRepository
from shared.infrastructure.messaging.kafka_producer import get_dispatcher
from shared.utils.create_service import create_service


dispatcher = get_dispatcher(kafka_topic_map="")


def message_queue_entrypoint():
    notification_input = request.get_json()
    service, uow = create_service(
        NotificationRepository, NotificationService, dispatcher=dispatcher
    )
    with uow:
        notification = Notification(**notification_input)
        service.send_notification(notification_input=notification)
        uow.register()

    return {"msg" : "notification sent"}

