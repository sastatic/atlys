from .base_database import BaseDatabaseStrategy
import json

class JsonFileDatabaseStrategy(BaseDatabaseStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add(self, new_data):
        existing_data = self.load()
        existing_data.append(new_data)
        self.save(existing_data)

    def update(self, key, new_data):
        existing_data = self.load()
        for item in existing_data:
            if item.get('key') == key:
                item.update(new_data)
                break
        self.save(existing_data)

    def delete(self, key):
        existing_data = self.load()
        existing_data = [item for item in existing_data if item.get('key') != key]
        self.save(existing_data)
