from django.db import models
from map.models import building

class event(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_name = models.CharField(max_length=100,null = False)
    details = models.TextField()
    buildingName = models.ForeignKey(building,on_delete=models.CASCADE)
    currently_on = models.BooleanField(default = False)
    event_time_date = models.TimeField(null = False)
    poster = models.ImageField(null=False,upload_to='Events/')
    organizor = models.CharField(max_length=100,null = False)
    contact_email = models.CharField(max_length=100,null = False)
    contact_cell = models.CharField(max_length=20,null = False)


    def __str__(self):
        return self.event_name
 
# TODO: Make url and view.py for events and meetups