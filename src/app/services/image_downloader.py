import os
import time
import requests
from urllib.parse import urlparse
from .image_storage_strategies import BaseImageStorage

def _get_image_extension_from_url(url: str) -> str:
    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[-1]

class ImageDownloader:
    def __init__(self, storage: BaseImageStorage):
        self.storage = storage

    def download_and_save_image(self, url: str) -> str:
        file_ext = _get_image_extension_from_url(url)
        file_path = self._generate_file_path(file_ext)
        image_data = self._download_image_data(url)
        self.storage.save_image(image_data, file_path)
        return file_path

    def _download_image_data(self, url: str):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            raise ValueError("Failed to download image from URL")

    def _generate_file_path(self, ext: str) -> str:
        output_dir = os.getenv('LOCAL_IMAGE_STORAGE_LOCATION')
        timestamp = int(time.time() * 1000)
        file_name = f"{timestamp}_output{ext}"
        file_path = os.path.join(output_dir, file_name)
        return file_path
    
