from pydantic import BaseModel, Field
from typing import Optional

class ScrapeRequest(BaseModel):
    url: Optional[str] = Field(None, description="URL for scraping")
    proxy_settings: Optional[str] = Field(None, description="Proxy Tool for scraping")
    num_pages: Optional[int] = Field(None, description="Number of pages to scrape")