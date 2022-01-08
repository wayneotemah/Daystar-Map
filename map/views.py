from django.shortcuts import render
from  .models import building,room

import folium


# Create your views here.
def index(request):
    


    #Post method
    if request.method=='POST':
        searchLocation = request.POST.get('locationSearch')
        block = building.objects.get(alias=searchLocation)
        m = folium.Map(location = [block.latitude,block.longitude],zoom_start=17)

        folium.Marker([block.latitude,block.longitude],tooltip=block.alias,
                    popup='<a href="info.html">More Info</a>',
                    icon=folium.Icon(color="blue", icon="info-sign")).add_to(m)
        m = m._repr_html_()
        context = {
        'm':m,
        'search':searchLocation
        }

        return render(request,'index.html',context)


    
    #GetMethod
    #creat map
    m = folium.Map(location = [-1.441190,37.047801],zoom_start=16)
    buildings = building.objects.all()
    for block in buildings:
        folium.Marker([block.latitude,block.longitude],tooltip=block.alias,
                    popup=block.name).add_to(m)
    
    m = m._repr_html_()
    context = {
        'm':m
    }

    return render(request,'index.html',context)