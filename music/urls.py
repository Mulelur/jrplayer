from django.urls import path
from .views import music_list


urlpatterns = [
    path('', music_list, name='music')
]