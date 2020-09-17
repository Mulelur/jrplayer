from django import forms
from cart.models import Transaction, Order

class UpdateStatusModelForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['status',]

class AddOrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['items',]