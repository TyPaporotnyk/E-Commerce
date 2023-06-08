from django.contrib import admin

from .models import (
    Order,
    OrderProduct,
    Customer,
    CustomerAddress
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address', 'get_product_count', 'created_at']
    list_display_links = ['id', 'customer']
    search_fields = ['id', 'customer']

    def get_product_count(self, obj):
        quantity = 0
        for product in obj.products.all():
            quantity += product.quantity

        return quantity
    
    get_product_count.short_description = 'Количество Товаров'
    

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'phone']
    list_display_links = ['email']
    search_fields = ['name', 'surname', 'email']

    def get_product_count(self, obj):
        return obj.products.count()


# @admin.register(CustomerAddress)
# class CustomerAddressAdmin(admin.ModelAdmin):
#     list_display = ['id']
#     list_display_links = ['id']
#     search_fields = ['id']

#     def get_product_count(self, obj):
#         return obj.products.count()

# @admin.register(OrderProduct)
# class OrderProductAdmin(admin.ModelAdmin):
#     list_display = ['id']