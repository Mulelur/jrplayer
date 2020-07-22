from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('album/', views.album, name='album'),
    path('album/<str:slug>/', views.album_detail, name='album-detail'),
    path('event/', views.event_list, name='event-list'),
    path('event/<str:slug>/', views.event_detail, name='event-detail'),
    path('news/', views.news, name='news'),
    path('news/<str:slug>/', views.news_detail, name='news-detail'),
    path('contact/', views.contact, name='contact')
]