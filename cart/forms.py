from django import forms
from .models import Order_model,Order_item_model


class Order_form(forms.ModelForm):
    payment_choice=(('COD','COD'),('ONLINE','ONLINE'))
    payment_method=forms.ChoiceField(choices=payment_choice)
    class Meta:
        model=Order_model
        fields=['address','phone','payment_method']