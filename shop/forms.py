from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category_model,Product_model


class Signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

        
        
class Login_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'enter username', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'enter password', 'class': 'form-control', 'id': 'password-field'})
    )

    
class Category_form(forms.ModelForm):
    class Meta:
        model=Category_model
        fields='__all__'
        
        
        
class Product_form(forms.ModelForm):
    class Meta:
        model=Product_model
        fields=['name','descriptions','image','price','stock','category']
        
        
class Add_stock_form(forms.ModelForm):
    class Meta:
        model=Product_model
        fields=['stock']
        