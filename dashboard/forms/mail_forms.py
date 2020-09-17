from django import forms
from dashboard.models import Mail

class MailModelForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'