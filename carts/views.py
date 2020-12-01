from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from products.models import Product, Variation


# Create your views here.
def view(request):
    try:
        _id = request.session['cart_id']
        cart = Cart.objects.get(id=_id)
    except:
        _id = None
    if _id:
        new_total = 0.00
        for item in cart.cartitem_set.all():
            brand_total = float(item.product.price) * item.quantity
            new_total += brand_total
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {'cart': cart}
    else:
        empty_message = "Your cart is empty, please shop with us."
        context = {"empty": True, "empty_message": empty_message}

    template = 'carts/view.html'
    return render(request, template, context)


def remove_from_cart(request, id):
    try:
        _id = request.session['cart_id']
        cart = Cart.objects.get(id=_id)
    except:
        return HttpResponseRedirect(reverse("cart_view"))
    cartitem = CartItem.objects.get(id=id)
    cartitem.cart = None
    cartitem.save()
    # Send success message
    return HttpResponseRedirect(reverse("cart_view"))


def add_to_cart(request, product_slug):
    request.session.set_expiry(900)
    try:
        _id = request.session['cart_id']
    except Exception:
        new_chart = Cart()
        new_chart.save()
        request.session['cart_id'] = new_chart.id
        _id = new_chart.id
    cart = Cart.objects.get(id=_id)
    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist as err:
        print(err)
    except Exception:
        pass

    product_var = []
    if request.method == 'POST':
        qty = request.POST['qty']
        if qty and int(qty) >= 0:
            for item in request.POST:
                if item != 'qty':
                    key = item
                    value = request.POST.get(key)
                    print(value)
                    try:
                        variation = Variation.objects.get(id=value)
                        product_var.append(variation)
                    except:
                        pass
            print(product_var)
            cart_item = CartItem.objects.create(cart=cart, product=product)
            if len(product_var) > 0:
                cart_item.variations.add(*product_var)
            cart_item.quantity = qty
            cart_item.save()
            # Success message
    # Error/failure message
    return HttpResponseRedirect(reverse("cart_view"))

