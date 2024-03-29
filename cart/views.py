from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from acconts.models import Profile
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order, Transaction
from .extras import generate_order_id
from .countrys import country, options
import stripe
from shop.models import Shop
from home.models import Banner

import datetime

stripe.api_key = ''

# def cart(request):
#     template = 'cart/cart.html'

#   
#     context = {
#      
#     }
#     return render(request, template, context)

def get_user_pending_order(request):
    # get order for the correct user
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)
        order = Order.objects.filter(owner=user_profile, is_ordered=False)
        if order.exists():
            # get the only order in the list of filtered orders
            return order[0]
        return 0
    else:
        return " "    


def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Shop.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if product in request.user.profile.product.all():
        messages.info(request, 'You already added this product')
        return redirect(reverse('shop-list')) 
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('shop'))



def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('order_summary'))



def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    banner = Banner.objects.get(title='cart')
    context = {
        'order': existing_order,
        'country': country,
        'options': options,
        'banner': banner
    }
    return render(request, 'cart/cart.html', context)


def checkout(request, **kwargs):
    existing_order = get_user_pending_order(request)
    if request.method == 'POST':
        
        token = request.POST['stripeToken']

        charge = stripe.Charge.create(
            amount=100*existing_order.get_cart_total(),
            currency='zar',
            description='buy',
            source=token,
        )
        return redirect(reverse('update_records', kwargs={'token': token}))
        
       
    context = {
        'order': existing_order,
    }

    return render(request, 'cart/checkout.html', context)



def update_transaction_records(request, token):
    # get the order being processed
    order_to_purchase = get_user_pending_order(request)

    # update the placed order
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
    order_to_purchase.save()
    
    # get all items in the order - generates a queryset
    order_items = order_to_purchase.items.all()

    # update order items
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    # Add products to user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # get the products from the items
    order_products = [item.product for item in order_items]
    user_profile.product.add(*order_products)
    user_profile.save()

    
    # create a transaction
    transaction = Transaction(profile=request.user.profile,
                            token=token,
                            order_id=order_to_purchase.id,
                            amount=order_to_purchase.get_cart_total(),
                            success=True)
    # save the transcation (otherwise doesn't exist)
    transaction.save()


    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    messages.info(request, "Thank you! Your purchase was successful!")
    return redirect(reverse('my_account'))


def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'cart/purchase_succes.html')