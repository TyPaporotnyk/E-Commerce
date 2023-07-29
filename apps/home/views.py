from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, ProductBrand, ProductType


def blank_path(request):
    return redirect("/home/all/")


def home_page_typed(request, type):
    if type == "all":
        products = Product.objects.all()
    else:
        product_type = get_object_or_404(ProductType, alternative_name=type)
        products = Product.objects.filter(product_type=product_type).all()

    # Filter by price
    # price_filter = request.GET.get("price")
    # if price_filter:
    #     if price_filter != "all":
    #         min_price, max_price = price_filter.split("-")
    #         products = products.filter(price__range=(min_price, max_price)).all()
    #
    # # Filter by brand
    # brand_filter = request.GET.get("brand")
    # if brand_filter:
    #     if brand_filter != "all":
    #         brand_filter = get_object_or_404(
    #             ProductBrand, alternative_name=brand_filter
    #         )
    #         products = products.filter(brand=brand_filter).all()
    #
    # # Sorting
    # sorting = request.GET.get("price_order")
    # if sorting:
    #     if sorting != "all":
    #         if sorting == "up":
    #             products = sorted(
    #                 products, key=lambda obj: obj.current_price(), reverse=False
    #             )
    #         if sorting == "down":
    #             products = sorted(
    #                 products, key=lambda obj: obj.current_price(), reverse=True
    #             )

    types_of_product = ProductType.objects.annotate(number_of_answers=Count("product"))
    types_of_product = list(
        sorted(types_of_product, key=lambda s: s.number_of_answers, reverse=True)
    )

    products_brand = ProductBrand.objects.all()

    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        template_name="home/home.html",
        context={
            "products": page_obj,
            "types_of_products": types_of_product,
            "products_brand": products_brand,
        },
    )


def product_page(request, uuid):
    product = get_object_or_404(Product, pk=uuid)
    return render(
        request,
        template_name="home/product.html",
        context={
            "product": product,
        },
    )
