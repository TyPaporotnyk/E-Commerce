from django.db import models

from src.product.models import Product


class Cart(models.Model):
    @property
    def price(self):
        return sum(
            map(lambda x: x.quantity * x.product.current_price, self.products.all())
        )

    @property
    def products_len(self):
        return sum(map(lambda x: x.quantity, self.products.all()))

    def __str__(self):
        return f"{self.id} - {self.products_len} - {self.price}"


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
