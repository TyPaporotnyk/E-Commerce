from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductView.as_view({"get": "list"})),
    path("<int:pk>/", views.ProductView.as_view({"get": "retrieve"})),
]
