from abc import ABC, abstractmethod

class BaseDatabaseStrategy(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def add(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass

