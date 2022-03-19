from django.contrib import admin
from .models import event

# Register your models here.
class eventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_time_date','buildingName','organizor')
    search_fields = ('event_name', 'event_time_date','buildingName','organizor')
    filter_fields = ('event_name', 'event_time_date','currently_on')
    list_select_related = ('buildingName',)
    #readonly_fields = ('latitude', 'longitude')

admin.site.register(event,eventAdmin)
