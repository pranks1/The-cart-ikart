from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Product_list, name='products'),
    url(r'^products/(?P<pk>\d+)$', views.product_detail, name='product_detail'),
    url(r'^categories/$', views.Category_list, name='category'),
    url(r'^category/(?P<pk>\d+)$', views.category_detail, name='category_detail'),
]