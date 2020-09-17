from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Shop
from django.contrib.auth.models import User
from cart.models import *

def shopFormView(request):
    # if request.method == 'POST':
    #     form = ShopForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    # else:
    #     form = ShopForm()

    # context = {
    #     'form':form
    # }
    # return render(request, 'admin/shop_form.html', context)
    pass

def shopFormUpdateView(request, slug):
    obj = get_object_or_404(Shop, slug=slug)

    form = ShopForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    
    context = {
        'form':form
    }
    return render(request, 'admin/shop_edit.html', context)

def shopFormDeleteView(request, slug):
    obj = get_object_or_404(Shop, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('shoplist')

    context = {}
    return render(request, 'admin/product.html', context)    



def profileView(request):
    context = {}

    return render(request, 'admin/profile.html', context)

def profileSettingsView(request):
    context = {}

    return render(request, 'admin/profile-settings.html', context)

def customersView(request):
    context = {}
    return render(request, 'dashboard/customers.html', context)

def supportsView(request):
    context = {}
    return render(request, 'dashboard/support.html', context)

