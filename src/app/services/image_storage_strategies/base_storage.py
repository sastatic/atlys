from abc import ABC, abstractmethod

class BaseImageStorage(ABC):
    @abstractmethod
    def save_image(self, image_data, filename):
        pass