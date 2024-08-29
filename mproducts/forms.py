from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','stockleft','price']

        widgets = {
            'stockleft': forms.TextInput(attrs={'placeholder': ''}),
        }