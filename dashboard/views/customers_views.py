from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from dashboard.models import Customers

def customers_view(request):
    template = 'dashboard/customers.html'
    customers = Customers.objects.filter(is_staff=False, is_superuser=False)
    context = {
        'customers': customers
    }
    return render(request, template, context)