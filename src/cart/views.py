from rest_framework import viewsets

from src.cart.serializers import CartSerializer, CartProductSerializer
from src.cart.utils import CartManager


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        return CartManager(self.request).get_cart()

    def get_object(self):
        return self.get_queryset()


class CartProductView(viewsets.ModelViewSet):
    serializer_class = CartProductSerializer

    def get_queryset(self):
        return CartManager(self.request).get_cart().products

    def perform_create(self, serializer):
        serializer.save(cart=CartManager(self.request).get_cart())
