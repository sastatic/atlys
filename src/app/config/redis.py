import os
import redis

REDIS_URI = os.getenv('REDIS_URI')

class Redis:
    def __init__(self) -> None:
        if REDIS_URI is None:
            raise ValueError("REDIS_URI environment variable is not set")
        self.client = redis.from_url(REDIS_URI)

    def set(self, key, value):
        self.client.set(key, value)

    def get(self, key):
        return self.client.get(key)

    def delete(self, key):
        self.client.delete(key)

    def exists(self, key):
        return self.client.exists(key)

    def expire(self, key, seconds):
        self.client.expire(key, seconds)
