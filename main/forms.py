from django import forms
from django.forms import DateTimeInput
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['instagram_nickname', 'pause', 'place']