from django.urls import reverse
from rest_framework.test import APITestCase


class CartCreationAPIViewTestCase(APITestCase):
    url = reverse("cart:list")

    def test_get_empty_cart(self):
        """
        Test to get empty cart
        """
        pass
