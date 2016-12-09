from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# Create your views here.
def Product_list(request):
    products = Product.objects.all()
    context_dict = {}
    context_dict['products'] = products
    return render(request, 'Catchdeal/product_list.html', context_dict)


def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'Catchdeal/product_detail.html', {'product': product})

def Category_list(request):
    category = Category.objects.all()
    return render(request, 'Catchdeal/category_list.html', {'category': category})

def category_detail(request,pk):
    categorys = get_object_or_404(Category, pk=pk)
    return render(request, 'Catchdeal/category_detail.html', {'categorys': categorys})



