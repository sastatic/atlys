from bs4 import BeautifulSoup
from app.models.product import Product

class Parser:
    def __init__(self, parser_type='html.parser', custom_rules=None):
        self.parser_type = parser_type
        self.custom_rules = custom_rules

    def parse(self, html_content):
        soup = BeautifulSoup(html_content, self.parser_type)
        if self.custom_rules:
            self.apply_custom_rules(soup)
        parsed_data, next_page = self.extract_data(soup)
        return parsed_data, next_page

    def apply_custom_rules(self, soup):
        pass

    def extract_data(self, soup):
        parsed_data = []
        products = soup.find_all("div", class_="product-inner")
        for product in products:
            img = product.find('img')
            title = img.attrs['title']
            image = img.attrs['data-lazy-src']
            price = product.find('span', class_='woocommerce-Price-amount')
            if price:
                price = float(price.text.strip('₹'))
            parsed_data.append(Product(product_title=title, product_price=price, path_to_image=image))
        next_page = soup.find('a', class_="next page-numbers")
        if next_page is not None:
            next_page = next_page.attrs['href']
        return parsed_data, next_page