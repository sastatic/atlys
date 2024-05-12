import requests
from typing import Optional

class Scraper:
    def __init__(self, user_agent=None, headers=None, proxies=None):
        self.user_agent = user_agent
        self.headers = headers
        self.proxies = proxies

        # Create a requests session
        self.session = requests.Session()
        if self.headers is not None:
            self.session.headers.update(self.headers)

    def scrape(self, url: str) -> Optional[requests.Response]:
        response = self.session.get(url, headers=self.headers, proxies=self.proxies)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to fetch data from {url}: {response.status_code}")
