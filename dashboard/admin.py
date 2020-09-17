from django.contrib import admin
# Register your models here.
from dashboard.models import Customers, Sale

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (('Personal info'), {'fields': ('ordered', 'phone', 'groups', 'user_permissions', 'last_order')}),
 
    )

admin.site.register(Customers, UserAdmin)
admin.site.register(Sale)