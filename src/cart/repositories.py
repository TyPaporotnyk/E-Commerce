from typing import Optional

from .models import Cart


class CartRepository:
    @staticmethod
    def get(cart_id) -> Optional[Cart]:
        return Cart.objects.get(pk=cart_id)

    @staticmethod
    def create() -> Cart:
        cart = Cart()
        cart.save()
        return cart

    @classmethod
    def get_or_create(cls, cart_id) -> Cart:
        if cart_id is None:
            return cls.create()

        cart = cls.get(cart_id)
        if cart is None:
            cart = cls.create()

        return cart
