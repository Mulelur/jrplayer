from django.urls import path
from .views import shop, shop_detail

urlpatterns = [
    path('', shop, name='shop'),
    path('<str:slug>/', shop_detail, name='shop-detail'),
]