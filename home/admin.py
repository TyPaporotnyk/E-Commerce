from django.contrib import admin
from .models import (
    Product,
    ProductType,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'product_type', 'price', 'quantity', 'created_at', 'updated_at']
    list_filter = ['product_type']
    list_display_links = ['title']
    search_fields = ['title']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    