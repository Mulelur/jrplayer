from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms.mail_forms import MailModelForm

def mail_view(request):
    template = 'dashboard/mail.html'
    context = {}
    return render(request, template, context)

def compose_view(request):
    template = 'dashboard/mail.html'
    form = MailModelForm(request.POST or None)
    context = {
        'compose_form': form
    }
    return render(request, template, context)

def inbox_view(request):
    template = 'dashboard/mail/inbox.html'    

    return render(request, template)