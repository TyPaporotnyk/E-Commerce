from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

from home.models import Product


class Order(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, verbose_name=_('Номер заказа'))
    products = models.ManyToManyField('OrderProduct', verbose_name=_('Продукты'))
    customer = models.ForeignKey('Customer',editable=True, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=_('Заказчик'))
    address = models.ForeignKey('CustomerAddress', editable=True, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=_('Адрес'))
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False, verbose_name=_('Дата обновления'))

    def __str__(self) -> str:
        return f'Заказ №{self.id}'

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')


class CustomerAddress(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    post_office = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.city}, {self.street} {self.house}, post:{self.post_office}'

    class Meta:
        verbose_name = _('Улица')
        verbose_name_plural = _('Улицы')


class Customer(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}, {self.phone}'

    class Meta:
        verbose_name = _('Заказчик')
        verbose_name_plural = _('Заказчики')


class OrderProduct(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, verbose_name=_('Айди товара для заказа'))
    product = models.ForeignKey(Product, editable=True, null=True, on_delete=models.CASCADE, verbose_name=_('Товар для заказа'))
    quantity = models.PositiveIntegerField(verbose_name=_('Количество'))

    def __str__(self) -> str:
        return f'{self.quantity}шт. {self.product.title}'