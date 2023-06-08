from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _


class ProductType(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, verbose_name=_('ID'))
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Название'))
    alternative_name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Альтернативное название'))
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Тип товара')
        verbose_name_plural = _('Типы товаров')


class ProductBrand(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, verbose_name=_('ID'))
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Название'))
    alternative_name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Альтернативное название'))
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Бренд')
        verbose_name_plural = _('Бренды')


class Product(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, verbose_name=_('ID'))
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Название'))
    description = models.TextField(blank=False, null=False, verbose_name=_('Описание'))
    product_type = models.ForeignKey(ProductType, editable=True, null=True, on_delete=models.SET_NULL, verbose_name=_('Тип товара'))
    brand = models.ForeignKey(ProductBrand, editable=True, null=True, on_delete=models.SET_NULL, verbose_name=_('Бренд'))
    img = models.ImageField(upload_to='uploads/products/img/', verbose_name=_('Изображение'))
    price = models.FloatField(blank=False, null=False, verbose_name=_('Цена'))
    discount_price = models.FloatField(blank=True, null=True, verbose_name=_('Скидочная цена'))
    quantity = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Количество'))
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False, verbose_name=_('Дата обновления'))
    


    def current_price(self):
        return self.price if not self.discount_price else self.discount_price

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = '-created_at',
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

