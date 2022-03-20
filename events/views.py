from django.shortcuts import render

# Create your views here.
def events(request):
    if request.method=='GET':
        return render(request,'eventlist.html')