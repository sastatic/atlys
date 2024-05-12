import os
import json
from typing import List
from app.models.product import Product
from app.scraper import Scraper, Parser, RetryMechanism
from app.database import DatabaseManager
from app.database.strategies import JsonFileDatabaseStrategy
from app.notification import NotificationManager
from app.notification.strategies import ConsoleNotificationStrategy
from app.config import Redis
from .image_downloader import ImageDownloader
from .image_storage_strategies import LocalImageStorage

class ScrapingService:
    def __init__(self):
        db_strategy = JsonFileDatabaseStrategy(os.getenv('JSON_FILE_LOCATION'))
        notification_strategy = ConsoleNotificationStrategy()
        storage = LocalImageStorage()
        self.downloader = ImageDownloader(storage)
        self.scraper = Scraper()
        self.parser = Parser()
        self.retry_mechanism = RetryMechanism()
        self.database_manager = DatabaseManager(db_strategy)
        self.notification_manager = NotificationManager(notification_strategy)
        self.redis = Redis()

    def scrape_website(self, url: str, page_count: int = 3) -> int:
        collected_data = []
        while url and page_count:
            try:
                cached_data = self.redis.get(url)
                if cached_data:
                    print("Fetched from cache")
                    cached_data = json.loads(cached_data.decode('utf-8'))
                    parsed_data = cached_data['parsed_data']
                    next_page = cached_data['next_page']
                else:
                    scraped_data = self.retry_mechanism.retry(lambda: self.scraper.scrape(url))
                    parsed_data, next_page = self.parser.parse(scraped_data)
                    parsed_data = self.jsonify_data(parsed_data)
                    redis_value = json.dumps({'parsed_data': parsed_data, 'next_page': next_page})
                    self.redis.set(key=url, value=redis_value)
                    self.redis.expire(url, 24*60*60)
                collected_data.extend(parsed_data)
                url = next_page
            except Exception as e:
                print(f"Error occurred during scraping: {e}")
                break  # Exit loop if an error occurs
            page_count -= 1
        self.database_manager.save_data(collected_data)
        self.notify_scraping_status(len(collected_data))
        return len(collected_data)
    
    def jsonify_data(self, collected_data: List[Product]):
        json_data = []
        for product in collected_data:
            product.path_to_image = self.downloader.download_and_save_image(product.path_to_image)
            json_data.append(product.jsonify())
        return json_data

    def notify_scraping_status(self, num_products_scraped: int):
        message = f"Scraping completed. Scraped {num_products_scraped} products."
        recipients = ["recipient1@example.com", "recipient2@example.com"]
        self.notification_manager.send_notification(recipients, message)

    def update_proxy(self) -> None:
        pass