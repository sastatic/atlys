from abc import ABC, abstractmethod

class BaseNotificationStrategy(ABC):
    @abstractmethod
    def send_notification(self, recipients, message):
        pass
