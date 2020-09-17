from django.urls import path
from .viewss import (shopFormView,
 profileView,
 profileSettingsView,
 shopFormUpdateView, 
 shopFormDeleteView,
 supportsView)
from dashboard.views.order_views import (OrderView,
    mark_as_delivered,
    update_status,
    filater,
    add_order,
    remove_order,
    search)
from dashboard.views.product_view import (
    ProductView,
    # edit_product,
    product_edit_view,
    view_product_view,
    product_order_view)
from dashboard.views.customers_views import(
    customers_view
)
from dashboard.views.mail_views import (
    mail_view,
    compose_view,
    inbox_view
)
from dashboard.views.settings_views import (
    settings_view
)
from dashboard.views.dashboard_views import (
    dashboard_view
)

app_name = 'dashboard'

urlpatterns = [
    # dasboard urls

    path('', dashboard_view, name='dashboard'), 


    path('shopform/', shopFormView, name='shopform'),
    path('product-list/', ProductView, name='shoplist'),
    path('product-list/<str:slug>/edit/', shopFormUpdateView, name='shop-update'),
    path('product-list/<str:slug>/remove/', shopFormDeleteView, name='shop-delete'),
    path('order-list/', OrderView, name='shop-order-list'),
    path('user-profile/', profileView, name='user-profile'),
    path('user-profile-settings/', profileSettingsView, name='user-profile-settings'),
    path('support/', supportsView, name='support'),
    path('mark_as_delivered/<int:id>/', mark_as_delivered, name='mark_as_delivered'),
    path('update_status/<id>', update_status, name='update_status'),
    path('filater/<q>/', filater, name='filater'),
    path('add_order/', add_order, name='add_order'),
    path('remove_order/<int:id>/', remove_order, name='remove_order'),
    path('search/', search, name='search'),

    # product urls

    # path('edit_product/<int:id>/', edit_product, name='edit_product'),
    path('edit_product_view/<int:id>/', product_edit_view, name='product_edit_view'),
    path('view_product/<int:id>/', view_product_view, name='view_product'),
    path('product_order/<int:id>/', product_order_view, name='product_order'),

    # Customers urls

    path('customers/', customers_view, name='customers'),

    # Mail urls

    path('mail/', mail_view, name='mail'),
    path('compose/', compose_view, name='compose'),
    path('inbox/', inbox_view, name='inbox'),

    # Settings urls

    path('settings/', settings_view, name='settings')
]