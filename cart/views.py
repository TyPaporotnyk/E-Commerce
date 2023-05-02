from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.core.serializers import serialize
from django.http import JsonResponse
import json

from .models import Order
from home.views import Product


def cart_page(request):    
    if not request.session.get('cart_products'):
        request.session['cart_products'] = []

    products_ids = request.session['cart_products']

    products = Product.objects.filter(id__in=products_ids).all()

    return render(request, template_name='cart/cart.html', context={'products': products})


@require_POST
def add_product_to_cart(request):
    # Get product
    data = json.load(request)
    product_id = data.get('product_id')

    if not request.session.get('cart_products'):
        request.session['cart_products'] = []

    request.session['cart_products'].append(product_id)

    print(request.session['cart_products'])
    request.session.modified = True

    return JsonResponse({'success': 'Product has ben added to cart'})


@require_http_methods(['DELETE'])
def delete_product_from_cart(request):
    if not request.session.get('cart_products'):
        return JsonResponse({'error': 'Product list is empty or not exist'})

    # Get product
    data = json.load(request)
    product_id = data.get('product_id')

    # Delete product from list
    request.session['cart_products'].remove(product_id)

    print(request.session['cart_products'])
    request.session.modified = True

    return JsonResponse({'success': 'Product has ben deleted'})
