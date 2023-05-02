from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_page, name='cart_page'),
    path('api/cart/add_to_cart/', views.add_product_to_cart, name='add_product_to_cart'),
    path('api/cart/delete_from_cart/', views.delete_product_from_cart, name='delete_product_from_cart'),
]