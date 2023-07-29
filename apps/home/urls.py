from django.urls import path

from . import views

urlpatterns = [
    path("", views.blank_path, name="blank_page"),
    path("home/", views.blank_path, name="home_page"),
    path("home/<str:type>/", views.home_page_typed, name="home_page_typed"),
    path("product/<uuid:uuid>/", views.product_page, name="product_page"),
]
