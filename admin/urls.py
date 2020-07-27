from django.urls import path
from .views import shopFormView, shopListView, shopOrderView, profileView, profileSettingsView, shopFormUpdateView, shopFormDeleteView

urlpatterns = [
    path('shopform/', shopFormView, name='shopform'),
    path('product-list/', shopListView, name='shoplist'),
    path('product-list/<str:slug>/edit/', shopFormUpdateView, name='shop-update'),
    path('product-list/<str:slug>/remove/', shopFormDeleteView, name='shop-delete'),
    path('order-list/', shopOrderView, name='shop-order-list'),
    path('user-profile/', profileView, name='user-profile'),
    path('user-profile-settings/', profileSettingsView, name='user-profile-settings'),

]