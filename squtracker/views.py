from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Squirrel

def get_map(request):
    sightings= Squirrel.objects.all()[:100]
    context ={
             'sightings':sightings,
              }  
    return render(request, 'squtracker/map.html', context)

def get_sightings(request):
    squirrels = Squirrel.objects.all()
    context ={
              'squirrels':squirrels,
               }
    return render(request, 'squtracker/sighsighs.html', context)

def detail(request,Unique_squirrel_ID):
    squirrel = get_object_or_404(Squirrel, pk =Unique_squirrel_ID)
    context ={
              'squirrel':squirrel,
               }
    return render(request, 'squtracker/squdetail.html', context)
def mainpage(request):
    return render(request, 'squtracker/mainpage.html')

