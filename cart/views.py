from django.shortcuts import render,redirect
from .models import Cart_model
from shop.models import Product_model
from django.views import View

class Add_to_cart(View):
    def get(self,request,i):
        p=Product_model.objects.get(id=i)
        u=request.user
        try:
            c=Cart_model.objects.get(user=u,product=p)
            c.quantity+=1
            c.save()
        except :
            c=Cart_model.objects.create(user=u,product=p,quantity=1)
            c.save()
        return redirect('shop:get-product',i=i)
    

class View_cart(View):
    def get(self,request):
        u=request.user
        c=Cart_model.objects.filter(user=u)
        total=0
        for i in c:
            total= total + i.product.price * i.quantity
        return render(request,'cart.html',{'cart':c,'total':total})
    
class Decrement_cart(View):
    def get(self,request,i):
        p=Cart_model.objects.get(id=i)
        if p.quantity>1:
            p.quantity-=1
            p.save()
        else:
            p.delete()
        return redirect('cart:view-cart')
    
    
    
    
class Increment_cart(View):
    def get(self,request,i):
        p=Cart_model.objects.get(id=i)
        p.quantity+=1
        p.save()
        return redirect('cart:view-cart')
    
class Delete(View):
    def get(self,request,i):
        p=Cart_model.objects.get(id=i)
        p.delete()
        return redirect('cart:view-cart')
        
        
class Checkout(View):
    def get(self,request):
        return render(request,'checkout.html')