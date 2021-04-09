from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Squirrel
from .forms import SquForm

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

def get_stats(request):
    return render(request, 'squtracker/stats.html')

def mainpage(request):
    return render(request, 'squtracker/mainpage1.html')

def addsqu(request):
    if request.method == "POST":
        form= SquForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/squtracker/sightings')
    else:
        form = SquForm()
    
    context ={
            'form':form,
        }
    return render(request,'squtracker/form.html',context)

def updatesqu(request,Unique_squirrel_ID):
    squirrel= Squirrel.objects.get(Unique_squirrel_ID=Unique_squirrel_ID)
    if request.method =='POST':
        form = SquForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/squtracker/sightings')
    else:
        form = SquForm(instance=squirrel)
    context ={
            'form':form,
             }
    return render(request, 'squtracker/form.html', context)


