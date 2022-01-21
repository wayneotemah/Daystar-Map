from django.shortcuts import render
from  .models import building,room,event,buildingPic
from .models import building as bld
import requests
import json

from django.conf import settings

get_location_api  = 'http://ip-api.com/json/'


# Create your views here.
def index(request):
    
    if request.method=='POST':
        searchLocation = request.POST.get('locationSearch')
        block = bld.objects.get(alias__contains=searchLocation)
        Name = block.name
        details = block.details
        blockPics = buildingPic.objects.filter(buildingName = block).first()

        # generate a list of names to be used as suggestions to users in searching
        buildings = bld.objects.all()
        suggestions = []
        for building in buildings:
            # suggestions.append(building.name)
            suggestions.append(str(building.alias))

        context = {
        "lat":block.latitude,
        "lon":block.longitude,
        'search':searchLocation,
        'buildingname':Name,
        'details':details, 
        'pics':blockPics,
        'suggestions':suggestions

        }

        return render(request,'index.html',context)


    #GetMethod
    #creat map
    if request.method=='GET':


        current_events = event.objects.all()
        eventName=''
        details=''
        eventime=''
 

        for event_ in current_events:
            if event.current_on:
                eventName = event_.name
                details = event_.details
                eventime = event_.evenTime
                building = event_.buildingName.name
                eventbuildingpics = buildingPic.objects.filter(buildingName = event_.buildingName).first()


        # generate a list of names to be used as suggestions to users in searching
        buildings = bld.objects.all()
        suggestions = []
        for building in buildings:
            # suggestions.append(building.name)
            suggestions.append(str(building.alias))

        print(suggestions)
        context = {
            "lat":-1.441190,
            "lon":37.047801,
            'eventName' : eventName,
            'details' : details,
            'eventime' : eventime,
            'buildingname':building,
            'pics':eventbuildingpics,
            'suggestions':suggestions

        }

        return render(request,'index.html',context)