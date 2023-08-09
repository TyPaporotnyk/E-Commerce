from django.urls import path

from . import views

urlpatterns = [
    path("", views.CartView.as_view({"get": "retrieve"})),
    path("products/", views.CartProductView.as_view({"post": "create"})),
    path(
        "products/<int:pk>/",
        views.CartProductView.as_view({"put": "update", "delete": "destroy"}),
    ),
]
