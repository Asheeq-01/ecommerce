from django.shortcuts import render,redirect
from django.views import View
from .models import Category_model,Product_model
from .forms import Signup_form,Login_form,Category_form,Product_form,Add_stock_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class catagorie(View):
    def get(self,request):
        b=Category_model.objects.all()
        return render(request,'catogorie.html',{'category':b})

class Product(View):
    def get(self,request,i):
        b=Category_model.objects.get(id=i)
        return render(request,'productpage.html',{'category':b})
    
    
class Get_product_details(View):
    def get(self,request,i):
        b=Product_model.objects.get(id=i)
        return render(request,'get_details.html',{'get':b})
    
    
    
    
    
    
class Signup(View):
    def get(self,request):
        form=Signup_form()
        return render(request,'signup.html',{'form':form})
    def post(self,request):
        form=Signup_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Signup successful!")
            return redirect('shop:login')
        return render(request, 'signup.html', {'form': form})


    
class Login(View):
    def get(self,request):
        form = Login_form()
        return render(request, 'login.html', {'form':form})

    def post(self,request):
        form = Login_form(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(request, username=u, password=p)

            if user is None:
                messages.error(request, "Invalid username or password")
                return redirect('shop:login')
            login(request, user)
            messages.success(request, "Login successful!")
            if user.is_superuser:
                return redirect('shop:shop')  # Admin page
            return redirect('shop:shop')  # Normal users redirect
        else:
            messages.error(request, "Form error!")
            return redirect('shop:login')

        
            
            
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('shop:login')


class Add_categories(View):
    def get(self,request):
        form=Category_form()
        return render(request,'add_categories.html',{'form':form})
    def post(self,request):
        form=Category_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('shop:add-categories')
    
    
class Add_product(View):
    def get(self,request):
        form=Product_form()
        return render(request,'add_product.html',{'form':form})
    def post(self,request):
        form=Product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('shop:add-product')
    
    
    
class Add_stock(View):
    def get(self,request,i):
        edit=Product_model.objects.get(id=i)
        form=Add_stock_form(instance=edit)
        return render(request,'add_stock.html',{'form':form})
    def post(self,request,i):
        edit=Product_model.objects.get(id=i)
        form=Add_stock_form(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect('shop:get-product',i=i)