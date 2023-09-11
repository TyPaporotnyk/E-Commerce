from django.urls import path

from src.order import views

urlpatterns = [
    path("", views.OrderView.as_view({"get": "list", "push": "create"})),
    path("<pk>/", views.OrderView.as_view({"get": "retrieve", "put": "update"})),
]
