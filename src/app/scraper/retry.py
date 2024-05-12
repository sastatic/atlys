import time

class RetryMechanism:
    def __init__(self, max_attempts=3, delay=1):
        self.max_attempts = max_attempts
        self.delay = delay

    def retry(self, func):
        for _ in range(self.max_attempts):
            try:
                response = func()
                return response
            except Exception as e:
                print("Error occurred:", e)
                print("Retrying...")
                time.sleep(self.delay)
        raise RuntimeError("Max retry attempts reached")
