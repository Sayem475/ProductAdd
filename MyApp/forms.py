from django import forms
from . models import ProductInfo

class Productform(forms.ModelForm):
    class Meta:
        model = ProductInfo
        fields = '__all__'