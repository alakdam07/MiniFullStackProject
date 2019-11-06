from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def products(request):
    productsDeatils = Product.objects.all()
    return render(request, 'products.html', {'products': productsDeatils})
