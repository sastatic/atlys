from fastapi import APIRouter
from app.services.scraping_service import ScrapingService
from app.models.scrape_request import ScrapeRequest

router = APIRouter()
scraping_service = ScrapingService()

DEFAULT_URL = "https://dentalstall.com/shop/"
DEFAULT_NUM_PAGES = 5
PROXY_SETTING = ""

@router.post("/scrape")
async def scraping_routes(request_data: ScrapeRequest):
    url = request_data.url if request_data and request_data.url else DEFAULT_URL
    num_pages = request_data.num_pages if request_data and request_data.num_pages else DEFAULT_NUM_PAGES
    if request_data and request_data.proxy_settings:
        scraping_service.update_proxy(request_data.proxy_settings)
    num_products_scraped = scraping_service.scrape_website(url, num_pages)
    return {"message": f"{num_products_scraped} products scraped"}