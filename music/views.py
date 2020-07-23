from django.shortcuts import render
from .models import Music
from django.core.paginator import Paginator
from cart.views import get_user_pending_order
from home.models import Banner

def music_list(request):
    existing_order = get_user_pending_order(request)
    music = Music.objects.all()
    banner = Banner.objects.get(title='music')

    paginator = Paginator(music, 10) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'music/music-list.html'
    context = {'order': existing_order,'page_obj': page_obj,'banner': banner, 'music': music}
    return render(request, template, context)

def music_detail(request):
    existing_order = get_user_pending_order(request)
    template = 'music/music-detail.html'
    context = {'order': existing_order,}

    return render(request, template, context)    
