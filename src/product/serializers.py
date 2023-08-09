from rest_framework import serializers

from src.product.models import (
    Product,
    ProductBrand,
    ProductImg,
    ProductSize,
    ProductType,
)


class ProductSizeSerializer(serializers.ModelSerializer):
    size = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductSize
        fields = ["id", "size"]


class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ["id", "img"]


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImgSerializer(many=True, read_only=True)
    sizes = ProductSizeSerializer(many=True, read_only=True)

    brand = serializers.StringRelatedField()
    product_type = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "brand",
            "product_type",
            "images",
            "sizes",
            "price",
            "discount_percent",
            "current_price",
            "quantity",
            "created_at",
            "updated_at",
        ]
