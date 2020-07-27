from django import forms
from shop.models import Shop

class ShopForm(forms.ModelForm):
    class Mate:
        model = Shop
        fields = '__all__'