from django.shortcuts import render
from home.models import About, Banner
from .models import Shop
from cart.views import get_user_pending_order
from django.core.paginator import Paginator

def shop(request):
    about = About.objects.all()
    shop = Shop.objects.all()
    existing_order = get_user_pending_order(request)
    banner = Banner.objects.get(title='shop')

    paginator = Paginator(shop, 10) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'shops': shop,
        'about': about,
        'banner': banner,
        'order': existing_order,
        'page_obj': page_obj,
    }
    return render(request, 'shop/shop.html', context) 


def shop_detail(request, slug):
    banner = Banner.objects.get(title='shop-detail')
    about = About.objects.all()
    existing_order = get_user_pending_order(request)
    shop = Shop.objects.get(slug=slug)
    related = Shop.objects.exclude(slug=slug)[:3]

    context = {
        'shop': shop,
        'about': about,
        'related': related,
        'banner': banner,
        'order': existing_order,
    }

    return render(request, 'shop/shop-detail.html', context) 
