from rest_framework import serializers

from src.order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "user",
            "email",
            "phone",
            "address",
            "products",
            "created_at",
            "updated_at",
        ]
