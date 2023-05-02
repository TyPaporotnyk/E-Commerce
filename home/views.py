from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from random import shuffle

from .models import (
    Product,
    ProductType,
)


def blank_path(request):
    return redirect('/home/all/')


def home_page_typed(request, type):
    if type == 'all':
        products = Product.objects.all()
    else:
        product_type = get_object_or_404(ProductType, alternative_name=type)
        products = Product.objects.filter(product_type=product_type).all()

    types_of_product = ProductType.objects.annotate(number_of_answers=Count('product'))
    types_of_product = list(sorted(types_of_product, key=lambda s: s.number_of_answers, reverse=True))

    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, 
        template_name='home/home.html',
        context={
            'products': page_obj,
            'types_of_products': types_of_product,
        }
    )


def home_page_price_typed(request, type, price):
    if type == 'all':
        products = Product.objects.all()
    else:
        product_type = get_object_or_404(ProductType, alternative_name=type)
        products = Product.objects.filter(product_type=product_type).all()

    types_of_product = ProductType.objects.annotate(number_of_answers=Count('product'))
    types_of_product = list(sorted(types_of_product, key=lambda s: s.number_of_answers, reverse=True))

    def filter_price(product , from_price, to_price):
        if product.discount_price:
            price = product.discount_price
        else:
            price = product.price

        return price > from_price and price <= to_price

    if price == '0-500':
        price_filter = lambda s: filter_price(s, 0, 500)
    elif price == '500-1000':
        price_filter = lambda s: filter_price(s, 500, 1000)
    elif price == '1000-3000':
        price_filter = lambda s: filter_price(s, 1000, 3000)
    else:
        price_filter = lambda s: s.price > 0

    products = list(filter(price_filter, products))

    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, 
        template_name='home/home.html',
        context={
            'products': page_obj,
            'types_of_products': types_of_product,
        }
    )


def product_page(request, uuid):
    product = get_object_or_404(Product, pk=uuid)
    return render(
        request, 
        template_name='home/product.html',
        context={
            'product': product,
        }
    )
