from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'landingpage.html')