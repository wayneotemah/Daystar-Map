from django.db import models

# Create your models here.
class building(models.Model):
    id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length=100,null = False)
    alias=models.CharField(max_length=15,null=False)  
    latitude = models.FloatField()
    longitude = models.FloatField()
    details = models.TextField()

    def __str__(self):
        return self.name

class room(models.Model):
    id = models.BigAutoField(primary_key=True)
    block = models.ForeignKey(building,on_delete=models.CASCADE)
    name= models.CharField(max_length=100,null = False)

    def __str__(self):
        return self.name 

class buildingPic(models.Model):
    id = models.BigAutoField(primary_key=True)
    picName = models.CharField(max_length=100,null = False)
    buildingName = models.ForeignKey(building,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.picName 
    
class event(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100,null = False)
    details = models.TextField()
    buildingName = models.ForeignKey(building,on_delete=models.CASCADE)
    current_on = models.BooleanField(default = False)
    evenTime = models.TimeField(null = False)

    def __str__(self):
        return self.name 


