from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('gallery/', include('gallery.urls')),
    path('shop/', include('shop.urls')),
    path('accont/', include('acconts.urls')),
    path('cart/', include('cart.urls')),
    path('music/', include('music.urls')),
    path('api/', include('api.urls'))
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)