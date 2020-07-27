from django.shortcuts import render, get_object_or_404, redirect
from .forms import ShopForm
from shop.models import Shop

def shopFormView(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ShopForm()

    context = {
        'form':form
    }
    return render(request, 'admin/shop_form.html', context)

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
def shopListView(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ShopForm()  


    shop_list = Shop.objects.all()
    
    context = {
        'shop_list': shop_list,
        'form': form
    }

    return render(request, 'admin/product.html', context)

def shopOrderView(request):

    context = {}

    return render(request, 'admin/ordes.html', context)

def profileView(request):
    context = {}

    return render(request, 'admin/profile.html', context)

def profileSettingsView(request):
    context = {}

    return render(request, 'admin/profile-settings.html', context)