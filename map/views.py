from django.shortcuts import render
from  .models import building,room,buildingPic
from events.models import event
from .models import building as bld
import requests
import json

from django.conf import settings




# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'landingpage.html')