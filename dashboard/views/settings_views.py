from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Setting
from dashboard.forms.settings_forms import SettingModelForm

def settings_view(request):
    template = 'dashboard/settings.html'
    setting,created = Setting.objects.get_or_create()
    form = SettingModelForm(request.POST or None, instance=setting)
    context = {
        'form': form
    }
    return render(request, template, context)