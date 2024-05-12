from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    product_title: Optional[str] = Field(None, description="Product Title")
    product_price: Optional[float] = Field(None, description="Product Price")
    path_to_image: Optional[str] = Field(None, description="Product Image")

    def jsonify(self):
        return {
            'product_title': self.product_title,
            'product_price': self.product_price,
            'path_to_image': self.path_to_image
        }