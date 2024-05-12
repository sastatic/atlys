from .base_notification import BaseNotificationStrategy

class ConsoleNotificationStrategy(BaseNotificationStrategy):
    def send_notification(self, recipients, message):
        print("Notification sent to:", recipients)
        print("Message:", message)