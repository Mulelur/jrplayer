from django.contrib import admin
import admin_thumbnails

from .models import (Event, New, Song, Album, Comment, Contact, Link, About, Reply, Banner)






# @admin_thumbnails.thumbnail('image')
# class ShopAdmin(admin.ModelAdmin):
# 	list_display = ['title','id','price']
# 	list_filter = ['title']
# 	inlines = [ShopImageInline]

@admin_thumbnails.thumbnail('image')
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','id','image','slug']
    prepopulated_fields = {'slug': ('title',)}



@admin_thumbnails.thumbnail('image')
class AlbumAdmin(admin.ModelAdmin):
	list_display = ['artist','id','title','slug','genre']
	prepopulated_fields = {'slug': ('title',)}


@admin_thumbnails.thumbnail('image')
class NewsAdmin(admin.ModelAdmin):
	list_display = ['title','id','slug']
	prepopulated_fields = {'slug': ('title',)}



class AboutAdmin(admin.ModelAdmin):
    list_display = ['image_tag','id']

	  

admin.site.register(Link)
admin.site.register(New,NewsAdmin)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Event,EventAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song)

admin.site.register(About,AboutAdmin)
admin.site.register(Reply)
admin.site.register(Banner)
