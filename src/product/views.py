from rest_framework import viewsets

from src.base.classes import Pagination
from src.product.models import Product
from src.product.seriallizers import ProductSerializer


class ProductView(viewsets.ReadOnlyModelViewSet):
    """
    Product list
    """

    serializer_class = ProductSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return Product.objects.prefetch_related("images", "sizes").all()
