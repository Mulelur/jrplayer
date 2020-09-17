from django.shortcuts import redirect, render, get_object_or_404
from shop.models import Shop, ColorVarient
from django.core.paginator import Paginator
from dashboard.forms.product_forms import UpdateProductModelForm
from django.contrib import messages
from cart.models import Order, OrderItem
from django.db.models import Q


def ProductView(request):

    shop_list = Shop.objects.all()
    form = UpdateProductModelForm()
    # paginator
    paginator = Paginator(shop_list, 10) 
    query = request.GET.get('page')

    page_obj = paginator.get_page(query)


    context = {
        'shop_list': shop_list,
        'page_obj': page_obj,
        'form': form
    }

    return render(request, 'dashboard/product.html', context)

def edit_product(request, id):
    product = get_object_or_404(Shop, id=id)
    form = UpdateProductModelForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, f'product updated')
        return redirect('shoplist')

def product_edit_view(request, id):
    product = get_object_or_404(Shop, id=id)
    template = 'dashboard/product_edit.html'
    form = UpdateProductModelForm(request.POST or None, instance=product)
    context = {
        'form': form,
        'product': product
    }
    return render(request, template, context)

def view_product_view(request, id):
    template = 'dashboard/product_view.html'

    product = get_object_or_404(Shop, id=id)
    colors = ColorVarient.objects.filter(product=product)
    context = {
        'product': product,
        'colors': colors
    }
    return render(request, template, context)

def product_order_view(request, id):
    template = 'dashboard/product_order.html'
    product = Shop.objects.get(id=id)
    order = OrderItem.objects.filter(product=product)
    
    context = {
        'order': order,
        'product': product
    }
    return render(request, template, context)