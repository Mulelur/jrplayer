from django.contrib import admin
import admin_thumbnails
from .models import Gallery



@admin_thumbnails.thumbnail('image')
class GalleryAdmin(admin.ModelAdmin):
	list_display = ['title','id','image_tag']

admin.site.register(Gallery,GalleryAdmin)