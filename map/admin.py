from django.contrib import admin
from  .models import building,room

# Register your models here.
class BuildingAdmin(admin.ModelAdmin):
    """Admin for driver reviews model"""

    list_display = ('name', 'alias', 'latitude','longitude')
    #search_fields = ('driver__account__username', 'user__account__username')
    # ordering = ('time_stamp',)
    # list_select_related = ('alias',)
    # readonly_fields = ('latitude', 'longitude')


class roomAdmin(admin.ModelAdmin):
    """Admin for driver reviews model"""

    list_display = ('name', 'block')
    #search_fields = ('driver__account__username', 'user__account__username')
    # ordering = ('time_stamp',)
    # list_select_related = ('name',)
    #readonly_fields = ('latitude', 'longitude')

admin.site.register(building,BuildingAdmin)
admin.site.register(room,roomAdmin)
