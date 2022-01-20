from django.shortcuts import render
from  .models import building,room,event,buildingPic
from .models import building as bld
import requests
import json

from django.conf import settings
# import folium

get_location_api  = 'http://ip-api.com/json/'


# Create your views here.
def index(request):
    
    if request.method=='POST':
        searchLocation = request.POST.get('locationSearch')
        block = bld.objects.get(alias__contains=searchLocation)
        Name = block.name
        details = block.details
        pics=[]
        blockPics = buildingPic.objects.filter(buildingName = block)
        for pic in blockPics:
            pics.append(pic)

        # m = folium.Map(location = [block.latitude,block.longitude],zoom_start=16.)
        # folium.Marker([block.latitude,block.longitude],tooltip=block.alias,
                # popup=Name).add_to(m)
        
        # m = m._repr_html_()

        context = {
        # 'm':m,
        "lat":block.latitude,
        "lon":block.longitude,
        'search':searchLocation,
        'Name':Name,
        'details':details, 
        'pics':pics
        }

        return render(request,'index.html',context)


    #GetMethod
    #creat map
    if request.method=='GET':

        # m = folium.Map(location = [-1.441190,37.047801],zoom_start=16.5)
        current_events = event.objects.all()
        eventName=''
        details=''
        eventime=''
        pics=[]

        for event_ in current_events:
            if event.current_on:
                eventName = event_.name
                details = event_.details
                eventime = event_.evenTime
                building = event_.buildingName.name
                eventbuildingpics = buildingPic.objects.filter(buildingName = event_.buildingName)
                for pic in eventbuildingpics:
                    pics.append(pic)

                # folium.Marker([event_.buildingName.latitude,event_.buildingName.longitude],tooltip=event_.buildingName.name,
                            # popup='On going activity').add_to(m)
        
        # m = m._repr_html_()
        
        context = {
            # 'm':m,
            "lat":-1.441190,
            "lon":37.047801,
            'eventName' : eventName,
            'details' : details,
            'eventime' : eventime,
            'building':building,
            'pics':pics,
        }

        return render(request,'index.html',context)