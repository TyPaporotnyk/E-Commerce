from django.contrib import admin
from .models import Order


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_product_count']
    list_display_links = ['id']
    search_fields = ['id']

    def get_product_count(self, obj):
        return obj.products.count()