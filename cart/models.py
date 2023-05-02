from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

from home.models import Product


class Order(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, verbose_name=_('Order ID'))
    products = models.ManyToManyField(Product, verbose_name=_('Продукты'))

    def __str__(self) -> str:
        return f'Заказ[{self.id}] : {self.products.count()} продуктов'

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
