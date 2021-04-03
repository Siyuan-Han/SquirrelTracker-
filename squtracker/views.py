from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Squirrel

def get_map(request):
    sightings= Squirrel.objects.all()[:100]
    context ={
             'sightings':sightings
              }  
    return render(request, 'squtracker/map.html', context)

def get_sightings(request):
    squirrels = Squirrel.objects.all()
    context ={
             'squirrels':squirrels
              }
    return render(request, 'squtracker/sighsighs.html', context)

