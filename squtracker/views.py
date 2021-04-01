from django.shortcuts import render
from django.shortcuts import render,redirect

def get_map(request):
   # sightings= Squirrel.objects.all()[:100]
   # context ={
   #         'sightings':sightings,
   #          }
    return render(request, 'squtracker/map.html', {}) # replace {} by content

