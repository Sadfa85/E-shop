from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Product, ProductAdmin)