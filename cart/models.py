from django.db import models
from django.contrib.auth.models import User
from shop.models import Product_model


class Cart_model(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product_model,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    def subtotal(self):
        return self.product.price*self.quantity
    
    
class Order_model(models.Model):
    order_id=models.CharField( max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    amount=models.IntegerField()
    address=models.TextField()
    phone=models.IntegerField()
    payment_method=models.CharField(max_length=50)
    ordered_date=models.DateTimeField(auto_now_add=True)
    is_order=models.BooleanField(default=False)
    delivery_status=models.CharField(default="pending")
    
    def __str__(self):
        return self.order_id
    
    
class Order_item_model(models.Model):
    order=models.ForeignKey(Order_model, on_delete=models.CASCADE,related_name='products')
    product=models.ForeignKey(Product_model, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    
    def __str__(self):
        return self.order.order_id