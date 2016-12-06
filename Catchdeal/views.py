from django.shortcuts import render
from .models import Product

# Create your views here.
def Product_list(request):
    products = Product.objects.all()
    return render(request, 'Catchdeal/product_list.html', {'products': products})


def product_detail(request):
    product = Product.objects.get(pk=)
    return render(request, 'Catchdeal/product_detail.html', {'products': products})
