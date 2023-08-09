from rest_framework import serializers

from src.cart.models import Cart, CartProduct


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "products", "price", "products_len"]
