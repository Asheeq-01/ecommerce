from django.contrib import admin
from .models import Category_model,Product_model
# Register your models here.
admin.site.register(Category_model)
admin.site.register(Product_model)