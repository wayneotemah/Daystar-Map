from django.db import models
from map.models import building

class meetup_and_hangout(models.Model):
    id = models.BigAutoField(primary_key=True)
    meetup_name = models.CharField(max_length=100,null = False)
    details = models.TextField()
    buildingName = models.ForeignKey(building,on_delete=models.CASCADE)
    currently_on = models.BooleanField(default = False)
    regular = models.BooleanField(default = False)
    meetup_time_date = models.TimeField(null = False)
    poster = models.ImageField(null=True,upload_to='Events/')
    organizor = models.CharField(max_length=100,null = False)
    contact_email = models.CharField(max_length=100,null = False)
    contact_cell = models.CharField(max_length=20,null = False)


    def __str__(self):
        return self.meetup_name 