from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Sale

def dashboard_view(request):
    template = 'dashboard/dashboard.html'
    dashboard = get_object_or_404(Sale, slug='sales')
    context = {
        'dashboard': dashboard
    }
    return render(request, template, context)