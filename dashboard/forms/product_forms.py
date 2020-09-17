from django import forms
from shop.models import *

class UpdateProductModelForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'

        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input', 'id':'customFile'}),
            'descirption': forms.Textarea(attrs={'class': 'form-control'})
        }


# class EditProductModelForm(forms.ModelForm):
#     class 