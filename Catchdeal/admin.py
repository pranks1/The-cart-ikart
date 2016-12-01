from django.contrib import admin
from .models import Product
from .models import Category
from .models import Attributes

# Register your models here.
class AtrributeAdmin(admin.ModelAdmin):
    list_display = ('size', 'price', 'color')
    list_filter = ('color',)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Attributes, AtrributeAdmin)