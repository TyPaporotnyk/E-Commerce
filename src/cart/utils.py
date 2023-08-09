from src.cart.repositories import CartRepository


class CartManager:
    def __init__(self, request):
        self.request = request

    def _set_cart_to_session(self, cart_id):
        self.request.session["cart"] = cart_id

    def get_cart(self):
        cart_id = self.request.session.get("cart")
        cart = CartRepository.get_or_create(cart_id)
        self._set_cart_to_session(cart.id)

        return cart
