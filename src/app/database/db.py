class DatabaseManager:
    def __init__(self, strategy):
        self._strategy = strategy

    def save_data(self, data):
        self._strategy.save(data)