from rest_framework import viewsets

from src.cart.repositories import CartProductRepository
from src.cart.serializers import CartProductSerializer, CartSerializer
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
        return CartProductRepository.get(CartManager(self.request).get_cart())

    def perform_create(self, serializer):
        serializer.save(cart=CartManager(self.request).get_cart())
