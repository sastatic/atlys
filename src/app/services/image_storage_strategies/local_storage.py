from .base_storage import BaseImageStorage

class LocalImageStorage(BaseImageStorage):
    def save_image(self, image_data, filename):
        with open(filename, 'wb') as f:
            f.write(image_data)