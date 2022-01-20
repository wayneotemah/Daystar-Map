from django.shortcuts import render
from  .models import building,room,event,buildingPic
from .models import building as bld
import requests
import json

from django.conf import settings
import folium

get_location_api  = 'http://ip-api.com/json/'

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
def index(request):
    
    if request.method=='POST':
        searchLocation = request.POST.get('locationSearch').lower()
        block = bld.objects.get(alias__contains=searchLocation)
        Name = block.name
        details = block.details
        pics=[]
        blockPics = buildingPic.objects.filter(buildingName = block)
        for pic in blockPics:
            pics.append(pic)

        m = folium.Map(location = [block.latitude,block.longitude],zoom_start=18)
        folium.Marker([block.latitude,block.longitude],tooltip=block.alias,
                popup=Name).add_to(m)
        
        m = m._repr_html_()
        context = {
        'm':m,
        'search':searchLocation,
        'Name':Name,
        'details':details, 
        'pics':pics
        }

        return render(request,'index.html',context)


    #GetMethod
    if request.method=='GET':

        # get user location
        ip = get_client_ip(request)
        res = requests.get(get_location_api+ip)
        user_data = res.text
        user_data = json.loads(user_data)
        userLat = user_data["lat"]
        userLon = user_data["lon"]



        # creat map 
        m = folium.Map(location = [userLat,userLon],zoom_start=17)
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

                folium.Marker([event_.buildingName.latitude,event_.buildingName.longitude],tooltip=event_.buildingName.name,
                            popup='On going activity').add_to(m)
        
        m = m._repr_html_()
        context = {
            'm':m,
            'eventName' : eventName,
            'details' : details,
            'eventime' : eventime,
            'building':building,
            'pics':pics,
        }

        return render(request,'index.html',context)