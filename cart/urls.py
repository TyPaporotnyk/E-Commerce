from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_page, name='cart_page'),
    path('order/success', views.order_page, name='order_page'),
    
    path('api/cart/add_to_cart/', views.add_product_to_cart, name='add_product_to_cart'),
    path('api/cart/delete_from_cart/', views.delete_product_from_cart, name='delete_product_from_cart'),
    path('api/cart/update_product_quantity/', views.update_product_quantity, name='update_product_quantity'),
    path('api/cart/make_order/', views.make_order, name='make_order'),
]