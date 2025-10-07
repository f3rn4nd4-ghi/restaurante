# resto/forms.py
from django import forms
from .models import Product, Customer, Service, ServiceItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'is_active']
        widgets = {
            'price': forms.NumberInput(attrs={'min': 0, 'step': 1})  # 👈 enteros
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['customer', 'notes']

class ServiceItemForm(forms.ModelForm):
    class Meta:
        model = ServiceItem
        fields = ['product', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'step': 1})
        }
