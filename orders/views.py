from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
from django.urls import reverse
from .models import Order
from .utils import id_generator
from django.contrib.auth.decorators import login_required


# Create your views here.
def orders(request):
    context = {}
    template = "orders/user.html"
    return render(request, template, context)


# Requires user login
@ login_required
def checkout(request):
    try:
        id = request.session['cart_id']
        cart = Cart.objects.get(id=id)
    except (KeyError, Cart.DoesNotExist):
        id = None
        return HttpResponseRedirect(reverse('cart_view'))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order(cart=cart)
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        # work on some error meassage
        return HttpResponseRedirect(reverse('cart_view'))

    # Assign address to the order
    if new_order.status == "completed":
        # cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('cart_view'))

    context = {}
    template = 'products/home.html'
    return render(request, template, context)
