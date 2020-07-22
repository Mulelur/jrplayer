from django.contrib import admin
from .models import Shop
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ShopAdmin(admin.ModelAdmin):
	list_display = ['title','image','image_tag']
	prepopulated_fields = {'slug': ('title',)}

@admin_thumbnails.thumbnail('image')
class ShopImageInline(admin.TabularInline):
	model = Shop
	readonly_fields = ('id',)
	extra = 1


admin.site.register(Shop,ShopAdmin)

