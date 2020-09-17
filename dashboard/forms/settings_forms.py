from django import forms
from dashboard.models import Setting

class SettingModelForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = '__all__'

        widgets = {
            'allow_registration': forms.RadioSelect(attrs={'class': 'custom-control-input', 'name': 'reg-public'}),
            'maintanance_mode': forms.CheckboxInput(attrs={'class': 'custom-control-input'})
        }