from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, ProductBrand, ProductType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "get_img",
        "title",
        "product_type",
        "price",
        "quantity",
        "created_at",
        "updated_at",
    ]
    list_filter = ["product_type", "brand"]
    list_display_links = ["title"]
    search_fields = ["title"]
    readonly_fields = ["get_img"]

    def get_img(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="175px" height="auto">')

    get_img.short_description = "Изображение товара"


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ["title"]
    search_fields = ["title"]


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]
