import json

from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods, require_POST

from apps.home.models import Product

from .forms import OrderForm
from .models import Customer, CustomerAddress, Order, OrderProduct


def cart_page(request):
    if request.session.get("cart_products") is None:
        request.session["cart_products"] = {}

    products_ids = request.session["cart_products"]

    products_quantity = [
        int(request.session["cart_products"][key]) for key in list(products_ids.keys())
    ]
    products = Product.objects.filter(id__in=products_ids).all()
    products = list(zip(products, products_quantity))
    order_form = OrderForm()

    context = {
        "products": products,
        "form": order_form,
    }
    return render(request, template_name="cart/cart.html", context=context)


@require_POST
def add_product_to_cart(request):
    # Get product
    data = json.load(request)
    product_id = data.get("product_id")

    if request.session.get("cart_products") is None:
        request.session["cart_products"] = {}

    if product_id not in request.session["cart_products"]:
        request.session["cart_products"][product_id] = 1

    else:
        product_quantity = request.session["cart_products"][product_id]
        if product_quantity < 10:
            request.session["cart_products"][product_id] = product_quantity + 1

    request.session.modified = True

    return JsonResponse({"success": "Product has ben added to cart"})


@require_http_methods(["UPDATE"])
def update_product_quantity(request):
    # Get product
    data = json.load(request)
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    # Set product quantity
    if not request.session.get("cart_products"):
        request.session["cart_products"] = {}
    request.session["cart_products"][product_id] = int(quantity)

    request.session.modified = True

    return JsonResponse({"success": "Product quantity has been updated"})


@require_http_methods(["DELETE"])
def delete_product_from_cart(request):
    if not request.session.get("cart_products"):
        return JsonResponse({"error": "Product list is empty or not exist"})

    # Get product
    data = json.load(request)
    product_id = data.get("product_id")

    # Delete product from list
    request.session["cart_products"].pop(product_id)

    request.session.modified = True
    return JsonResponse({"success": "Product has been deleted"})


@require_POST
def make_order(request):
    order_form = OrderForm(request.POST)

    if not order_form.is_valid():
        for field, errors in order_form.errors.items():
            return JsonResponse({"message": errors}, status=400)

    data = order_form.cleaned_data

    # Get all products by order
    cart_products = request.session["cart_products"]
    products_ids = list(cart_products.keys())
    products = Product.objects.filter(id__in=products_ids)

    # Create new ProductsOrder by products ids
    order_products = []
    for product in products:
        o_product = OrderProduct.objects.create(
            product=product, quantity=cart_products[str(product.id)]
        )
        o_product.save()
        order_products.append(o_product)

    # # Create new Customer if not exist
    customer = Customer.objects.filter(
        Q(email=data["email"]) & Q(phone=data["phone_number"])
    ).first()
    if not customer:
        customer = Customer.objects.create(
            name=data["name"],
            surname=data["surname"],
            email=data["email"],
            phone=data["phone_number"],
        )
        customer.save()

    customer_address = CustomerAddress.objects.create(
        city=data["city"],
        street=data["street"],
        house=data["house_number"],
        post_office=data["post_office"],
    )
    customer_address.save()

    # Create Order and put ProductsOrders on it
    order = Order.objects.create(
        customer=customer,
        address=customer_address,
    )
    order.products.add(*order_products)
    order.save()

    request.session["cart_products"].clear()
    request.session["order_id"] = order.id.hex
    request.session.modified = True

    return JsonResponse(
        {"success": "Order has been created successfully", "order_id": order.id}
    )


def order_page(request):
    order_id = request.session.get("order_id")
    if not order_id:
        raise Http404()

    request.session["order_id"] = ""
    request.session.modified = True

    order = get_object_or_404(Order, id=order_id)
    return render(request, template_name="cart/success.html", context={"order": order})
