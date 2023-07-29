from rest_framework import serializers

from src.product.models import Product, ProductImg, ProductSize


class ProductSizeSerializer(serializers.ModelSerializer):
    size = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductSize
        fields = ["id", "size"]


class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ["id", "img"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImgSerializer(many=True, read_only=True)
    sizes = ProductSizeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "images",
            "sizes",
            "price",
            "discount_percent",
            "quantity",
            "created_at",
            "updated_at",
        ]
