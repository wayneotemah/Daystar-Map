from django.contrib import admin
from  .models import building,room,buildingPic,event

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
    
    list_display = ('name',)
    #search_fields = ('driver__account__username', 'user__account__username')
    # ordering = ('time_stamp',)
    # list_select_related = ('name',)
    #readonly_fields = ('latitude', 'longitude')

class picsAdmin(admin.ModelAdmin):
    list_display = ('picName', 'buildingName')
    search_fields = ('buildingName',)


class eventAdmin(admin.ModelAdmin):
    list_display = ('name', 'evenTime','buildingName')
    search_fields = ('buildingName',)


admin.site.register(building,BuildingAdmin)
admin.site.register(room,roomAdmin)
admin.site.register(buildingPic,picsAdmin)
admin.site.register(event,eventAdmin)

