from django.contrib import admin

from src.cart.models import Cart, CartProduct

admin.site.register(Cart)
admin.site.register(CartProduct)
