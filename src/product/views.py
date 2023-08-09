from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from src.base.classes import Pagination
from src.product.models import Product, ProductBrand, ProductType
from src.product.serializers import (
    ProductBrandSerializer,
    ProductSerializer,
    ProductTypeSerializer,
)


class ProductView(viewsets.ReadOnlyModelViewSet):
    """
    Product list
    """

    queryset = Product.objects.prefetch_related("images", "sizes")
    serializer_class = ProductSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["product_type__name", "brand__name"]


class ProductTypeView(viewsets.ReadOnlyModelViewSet):
    """
    Product type list
    """

    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductBrandView(viewsets.ReadOnlyModelViewSet):
    """
    Product brand list
    """

    serializer_class = ProductBrandSerializer
    queryset = ProductBrand.objects.all()
