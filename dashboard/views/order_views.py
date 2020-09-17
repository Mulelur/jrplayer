from django.shortcuts import render, redirect, get_object_or_404
from cart.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from dashboard.forms.order_forms import UpdateStatusModelForm, AddOrderModelForm
from django.db.models import Q


def OrderView(request):
    transaction = Transaction.objects.all()
    form = UpdateStatusModelForm()

    paginator = Paginator(transaction, 10) 
    query = request.GET.get('page')

    page_obj = paginator.get_page(query)

    context = {
        'transaction': transaction,
        'page_obj': page_obj,
        'form': form
    }

    return render(request, 'dashboard/ordes.html', context)

def mark_as_delivered(request, id):
    transaction = Transaction.objects.get(id=id)
    obj = transaction
    if obj.status != 'Delivered':
        obj.status = 'Delivered'
        obj.save()
        messages.success(request, f'marked as delivered')
    else:
        messages.warning(request, f'already mark as delivered')
    return redirect('shop-order-list')

def update_status(request, id):
    transaction = Transaction.objects.get(id=id)
    form = UpdateStatusModelForm(request.POST or None, instance=transaction)
    if form.is_valid():
        form.save()
        messages.success(request, f' Status Succesfuly Updated')
    else:
        messages.warning(request, f'already mark as delivered')
    return redirect('shop-order-list')

def filater(request, q):
    print(q)
    transaction = Transaction.objects.filter(status=q)

    paginator = Paginator(transaction, 10) 
    query = request.GET.get('page')

    page_obj = paginator.get_page(query)
    form = UpdateStatusModelForm()
    add_order_form = AddOrderModelForm()
    context = {
        'page_obj': page_obj,
        'form': form,
        'add_order_form': add_order_form
    }

    return render(request, 'dashboard/ordes.html', context)

def add_order(request):
    add_order_form = AddOrderModelForm(request.POST or None)
    if add_order_form.is_valid():
        add_order_form.save()
        return redirect('filater')

def remove_order(request, id):
    order_remove = get_object_or_404(Transaction, id=id)

    order_remove.delete()
    messages.success(request, f'order removed')
    return redirect('shop-order-list')
    
def search(request):
    template = 'dashboard/ordes.html'
    query = request.GET.get('q')
    if query:
        results = Transaction.objects.filter(Q(id__icontains=query) | Q(order_id__icontains=query))
    else:
        results = Transaction.objects.all()

    Qs = request.GET.get('page')
    paginator = Paginator(results, 10) # Show 10 contacts per page.
    page_obj = paginator.get_page(Qs)
    return render(request, template, {'page_obj': page_obj, 'query': query})