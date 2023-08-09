from rest_framework import viewsets

from src.order.models import Order
from src.order.serializers import OrderSerializer


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()
