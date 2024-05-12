from .base_notification import BaseNotificationStrategy

class SlackNotificationStrategy(BaseNotificationStrategy):
    def send_notification(self, recipients, message):
        # Implement Slack notification logic here
        pass