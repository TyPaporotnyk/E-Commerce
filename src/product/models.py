from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from src.base.services import (
    delete_old_file,
    get_new_product_img_path,
    validate_size_image,
)


class Product(models.Model):
    title = models.CharField(
        max_length=50, blank=False, null=False, verbose_name=_("Название")
    )

    product_type = models.ForeignKey(
        "ProductType",
        editable=True,
        null=True,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        "ProductBrand",
        editable=True,
        null=True,
        on_delete=models.CASCADE,
    )

    price = models.FloatField(blank=False, null=False, verbose_name=_("Цена"))
    discount_percent = models.FloatField(default=0, verbose_name=_("Процент скидки"))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_("Количество"))

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    @property
    def current_price(self):
        return (
            self.price - (self.price / 100 * self.discount_percent)
            if self.discount_percent
            else self.price
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("-created_at",)


class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} {self.size}"


class ProductImg(models.Model):
    img = models.ImageField(
        upload_to=get_new_product_img_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            validate_size_image,
        ],
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )


class ProductType(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class ProductBrand(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


@receiver(post_delete, sender=ProductImg)
def delete_file_on_delete(sender, instance, **kwargs):
    """
    Auto delete file after deleting model
    """
    if instance.img:
        delete_old_file(instance.img.path)


@receiver(pre_save, sender=ProductImg)
def delete_file_on_change(sender, instance, **kwargs):
    """
    Delete file if uploaded file is different on change.
    """
    if not instance.pk:
        return False

    try:
        old_file = ProductImg.objects.get(pk=instance.pk).img
    except ProductImg.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        delete_old_file(old_file.path)
