from django.urls import path
from .views import shopFormView, shopListView, shopOrderView

urlpatterns = [
    path('shopform/', shopFormView, name='shopform'),
    path('product-list/',shopListView, name='shoplist'),
    path('order-list/', shopOrderView, name='shop-order-list')
]