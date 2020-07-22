from django.forms import ModelForm
from .models import Contact, Comment

class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','title','email','text']

class RelpayForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','reply']        
