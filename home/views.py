from django.shortcuts import render
from .forms import ContactModelForm, CommentForm, RelpayForm
from gallery.models import Gallery
from cart.models import Order
from django.core.paginator import Paginator
from cart.views import get_user_pending_order

from .models import (Event, New, Song, Album, Comment, Contact, Link, About, Banner)


def home(request):
    event = Event.objects.all()
    album = Album.objects.all()
    news = New.objects.all()
    about = About.objects.all()
    photo = Gallery.objects.all()[1:6]
    existing_order = get_user_pending_order(request)
    context = {
        'events': event,
        'albums': album,
        'news': news,
        'about': about,
        'photos': photo,
        'order': existing_order,
    }
    return render(request, 'home/home.html', context)


def album(request):
    existing_order = get_user_pending_order(request)
    album = Album.objects.all()
    about = About.objects.all()
    paginator = Paginator(album, 10) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    banner = Banner.objects.get(title='album')

    context = {
        'albums': album,
        'about': about,
        'banner': banner,
        'order': existing_order,
        'page_obj': page_obj,
    }

    return render(request, 'album/album-list.html', context)

def album_detail(request, slug):
    song = Song.objects.all()
    existing_order = get_user_pending_order(request)
    about = About.objects.all()
    album = Album.objects.get(slug=slug)
    banner = Banner.objects.get(title='album-detail')

    context = {
        'song': song,
        'album': album,
        'about': about,
        'banner': banner,
        'order': existing_order,
    }
    return render(request, 'album/album-detail.html', context)

def event_detail(request, slug):
    about = About.objects.all()
    existing_order = get_user_pending_order(request)
    event = Event.objects.get(slug=slug)
    
    banner = Banner.objects.get(title='event-detail')
    context = {
        'event': event,
        'about': about,
        'banner': banner,
        'order': existing_order,
    }
    return render(request, 'event/event-detail.html', context)


def event_list(request):
    about = About.objects.all()
    event = Event.objects.all()
    paginator = Paginator(event, 10) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    existing_order = get_user_pending_order(request)
    banner = Banner.objects.get(title='event-list')

    context = {
        'events': event,
        'about': about,
        'banner': banner,
        'order': existing_order,
        'page_obj': page_obj,
    }

    return render(request, 'event/event-list.html', context)  

def news(request):
    about = About.objects.all()
    news = New.objects.all()
    

    paginator = Paginator(news, 10) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    existing_order = get_user_pending_order(request)
    banner = Banner.objects.get(title='news')
    context = {
        'news': news,
        'about': about,
        'banner': banner,
        'order': existing_order,
        'page_obj': page_obj,
    }
    return render(request, 'news/news-list.html', context) 

def news_detail(request, slug):
    about = About.objects.all()
    existing_order = get_user_pending_order(request)
    banner = Banner.objects.get(title='news-detail')

    news = New.objects.get(slug=slug)
    recent = New.objects.order_by()
    form = CommentForm()
    form_reply = RelpayForm(instance=news)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form_reply = RelpayForm(request.POST, instance=news)
        if form.is_valid() and form_reply.is_valid():
            form.save()
            form_reply.save()

    comments = New.objects.all()      
    

    context = {
        'news': news,
        'form': form,
        'comments': comments,
        'about': about,
        'banner': banner,
        'order': existing_order,
    }
    return render(request, 'news/news-detail.html', context)           


def contact(request):
    existing_order = get_user_pending_order(request)
    about = About.objects.all()
    banner = Banner.objects.get(title='contact')
    form = ContactModelForm()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'about': about,
        'banner': banner,
        'order': existing_order,
    }        
    return render(request, 'contact/contact.html', context)
