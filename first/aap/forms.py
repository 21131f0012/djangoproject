from django import forms
from .models import products

class ProductSearchForm(forms.Form):
    class Meta:
        model = products
        fields =['medicine','price','manufacture_date','expiry','quantity']


    

