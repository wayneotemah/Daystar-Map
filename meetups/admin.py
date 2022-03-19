from django.contrib import admin
from .models import meetup_and_hangout

# Register your models here.
class meetup_and_hangoutAdmin(admin.ModelAdmin):
    list_display = ('meetup_name', 'meetup_time_date','buildingName','organizor')
    search_fields = ('meetup_name', 'meetup_time_date','buildingName','organizor')
    filter_fields = ('meetup_name', 'meetup_time_date','buildingName','currently_on')
    list_select_related = ('buildingName',)
    #readonly_fields = ('latitude', 'longitude')

admin.site.register(meetup_and_hangout,meetup_and_hangoutAdmin)
