from django.contrib import admin
from .models import Category, Product, ProductAttribute, ProductType, ProductImage
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductType)
admin.site.register(ProductImage)
