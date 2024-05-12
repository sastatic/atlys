from .base_notification import BaseNotificationStrategy

class EmailNotificationStrategy(BaseNotificationStrategy):
    def send_notification(self, recipients, message):
        # Implement email notification logic here
        pass