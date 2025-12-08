from django.shortcuts import render,redirect
from .models import Cart_model,Order_model,Order_item_model
from shop.models import Product_model
from django.views import View
from .forms import Order_form
import razorpay
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.contrib.auth.decorators import login_required


@method_decorator(login_required,name="dispatch")
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
    


@method_decorator(login_required,name="dispatch")
class View_cart(View):
    def get(self,request):
        u=request.user
        c=Cart_model.objects.filter(user=u)
        total=0
        for i in c:
            total= total + i.product.price * i.quantity
        return render(request,'cart.html',{'cart':c,'total':total})
    

@method_decorator(login_required,name="dispatch")
class Decrement_cart(View):
    def get(self,request,i):
        p=Cart_model.objects.get(id=i)
        if p.quantity>1:
            p.quantity-=1
            p.save()
        else:
            p.delete()
        return redirect('cart:view-cart')
    
    
    

@method_decorator(login_required,name="dispatch")
class Increment_cart(View):
    def get(self,request,i):
        p=Cart_model.objects.get(id=i)
        p.quantity+=1
        p.save()
        return redirect('cart:view-cart')


@method_decorator(login_required,name="dispatch")
class Delete(View):
    def get(self,request,i):
        p=Cart_model.objects.get(id=i)
        p.delete()
        return redirect('cart:view-cart')
        
@method_decorator(login_required,name="dispatch")
class Checkout(View):
    def get(self,request):
        form=Order_form()
        return render(request,'checkout.html',{'form':form})
    
    
    def post(self,request):
        form=Order_form(request.POST)
        if form.is_valid():
            o=form.save(commit=False)
            u=request.user
            o.user=u
            c=Cart_model.objects.filter(user=u)
            total=0
            for i in c:
                total+=i.subtotal()
            print(total)
            o.amount=total
            o.save()
            if (o.payment_method=="ONLINE"):
                client=razorpay.Client(auth=('rzp_test_Rn84wf6yM1UDDU','HaEkeKGDEGJDSIU24uFKoffZ'))
                response_payment=client.order.create({'amount':o.amount*100,'currency':'INR'})
                print(response_payment)
                id=response_payment['id']
                o.order_id=id
                o.save()
            
                return render(request,'payment.html',{'payment':response_payment})
            else:
                id='ORD_ID'+uuid.uuid4().hex[:14]
                o.order_id=id
                o.is_order=True
                o.save()
                for i in c:
                    item=Order_item_model.objects.create(order=o,product=i.product,quantity=i.quantity)
                    item.save()
                    item.product.stock-=i.quantity
                    item.product.save()
                    c.delete()
                    return render(request,'payment.html')
    
    
@method_decorator(login_required,name="dispatch")
@method_decorator(csrf_exempt,name='dispatch')    
class Payment_success(View):
    def post(self,request):
        response=request.POST
        print(response)
        id=response['razorpay_order_id']
        o=Order_model.objects.get(order_id=id)
        o.is_order=True
        o.save()
        
        u=request.user
        c=Cart_model.objects.filter(user=u)
        for i in c:
            item=Order_item_model.objects.create(order=o,product=i.product,quantity=i.quantity)
            item.save()
            item.product.stock-=i.quantity
            item.product.save()
            
        c.delete()
        return render(request,'payment_success.html')
    def get(self,request):
        return render(request,'payment_success.html')
    
    
    
    
    
    
    
@method_decorator(login_required,name="dispatch")
class My_order(View):
    def get(self,request):
        u=request.user
        o=Order_model.objects.filter(user=u,is_order=True)
        return render(request,'myorder.html',{'orders':o})