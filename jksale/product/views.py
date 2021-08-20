from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product, ProductImage
# Create your views here.


def shopView(request):
    category = Category.objects.all()
    product =  Product.objects.all()
    context = {
        'category':category,
        'product':product,
    }
    return render(request, 'shop.html', context)

def productView(request, slug):
    product =  Product.objects.get(slug=slug)
    context = {
        'products':product,
    }
    return render(request, 'product.html', context)

