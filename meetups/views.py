from django.shortcuts import render

# Create your views here.
def meetup(request):
    if request.method=='GET':
        return render(request,'discoverlistpage.html')