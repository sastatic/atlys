from app.notification.strategies import BaseNotificationStrategy

class NotificationManager:
    def __init__(self, notification_strategy: BaseNotificationStrategy):
        self._notification_strategy = notification_strategy

    def send_notification(self, recipients, message):
        self._notification_strategy.send_notification(recipients, message)