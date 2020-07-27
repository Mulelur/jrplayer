from django.shortcuts import render
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

def shopListView(request):
    
    shop_list = Shop.objects.all()
    context = {
        'shop_list': shop_list
    }

    return render(request, 'admin/product.html', context)

def shopOrderView(request):

    context = {}

    return render(request, 'admin/ordes.html', context)

