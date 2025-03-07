from django import forms
from .models import Product


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
    
class Products(forms.Form):
    productName = forms.CharField(label="Name", max_length=200)
    productDesc = forms.CharField(label="Description", max_length=200)
    productPrice = forms.DecimalField(label="Price", max_digits=10, decimal_places=2)
    productImage = forms.ImageField(allow_empty_file=True)