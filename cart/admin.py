from django.contrib import admin
from .models import Cart_model,Order_item_model,Order_model

admin.site.register(Cart_model)
admin.site.register(Order_model)
admin.site.register(Order_item_model)
