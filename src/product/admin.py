from django.contrib import admin

from .models import Product, ProductBrand, ProductImg, ProductSize, ProductType, Size


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
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


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]


admin.site.register(ProductImg)
admin.site.register(ProductSize)
admin.site.register(Size)
