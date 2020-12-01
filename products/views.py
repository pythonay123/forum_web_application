from django.shortcuts import render
from django.urls import reverse
from .models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


# Create your views here.
def home(request):
    all_products = Product.objects.all()
    template = 'products/home.html'
    context = {'products': all_products}
    return render(request, template, context)


def all(request):
    all_products = Product.objects.all()
    context = {'products': all_products}
    template = 'products/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        prod_images = product.productimage_set.all()
        context = {'product': product, 'prod_images': prod_images}
        template = 'products/single.html'
        return render(request, template, context)
    except ObjectDoesNotExist:
        raise Http404


def search(request):
    try:
        k = request.GET.get('k')
    except Exception:
        k = None
    if k:
        products = Product.objects.filter(title__icontains=k)
        context = {'query': k, 'products': products}
        template = 'products/results.html'
    else:
        context = {}
        template = 'products/home.html'
    return render(request, template, context)
