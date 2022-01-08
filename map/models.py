from django.db import models

# Create your models here.
class building(models.Model):
    id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length=100,null = False)
    alias=models.CharField(max_length=5,null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class room(models.Model):
    id = models.BigAutoField(primary_key=True)
    block = models.ForeignKey(building,on_delete=models.CASCADE)
    name= models.CharField(max_length=100,null = False)

    def __str__(self):
        return self.name 
    