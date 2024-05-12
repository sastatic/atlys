import os
from dotenv import load_dotenv
from app.services.scraping_service import ScrapingService



def test_scraping_service():
    scraping_service = ScrapingService()
    url = 'https://dentalstall.com/shop/'
    num_products_scraped = scraping_service.scrape_website(url)
    print(f"Number of products scraped: {num_products_scraped}")

if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)
    test_scraping_service()
