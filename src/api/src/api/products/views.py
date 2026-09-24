from django.shortcuts import render

from .models import Product


# Create your views here.
def product_list(request: None):
    products = Product.objects.all()
    render(request, "", {"product": products})
