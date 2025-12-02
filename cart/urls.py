"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart import views

app_name='cart'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-to-cart/<int:i>/',views.Add_to_cart.as_view(),name="add-to-cart"),
    path('viewcart/',views.View_cart.as_view(),name="view-cart"),
    path('decriment/<int:i>/',views.Decrement_cart.as_view(),name="decrement"),
    path('incriment/<int:i>/',views.Increment_cart.as_view(),name="increment"),
    path('delete/<int:i>/',views.Delete.as_view(),name="delete"),
    path('checkout/',views.Checkout.as_view(),name="checkout"),
    
]
