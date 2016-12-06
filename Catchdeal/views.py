from django.shortcuts import render
from .models import Product
# Create your views here.
def Product_list(request):
    products = Product.objects.all()
    return render(request, 'Catchdeal/product_list.html', {'products': products})
