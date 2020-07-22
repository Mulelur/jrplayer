from django.shortcuts import render
from .models import Gallery
from home.models import Banner
from cart.views import get_user_pending_order
from django.core.paginator import Paginator

def gallery(request):
    gallery = Gallery.objects.all()
    gallerys = Gallery.objects.all()[:5]
    existing_order = get_user_pending_order(request)
    banner = Banner.objects.get(title='gallery')

    paginator = Paginator(gallery, 10) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'gallery/photos.html'
    context = {
        'gallery': gallery,
        'banner': banner,
        'gallerys': gallerys ,
        'order': existing_order,
        'page_obj': page_obj,
    }
    return render(request, template, context)
