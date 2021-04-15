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
    squirrels = Squirrel.objects.all()
    total = Squirrel.objects.all().count()
    number_AM = squirrels.filter(Shift = 'AM').count()
    number_PM = squirrels.filter(Shift = 'PM').count()
    percent_AM = number_AM/squirrels.count()
    percent_AM = "{:.2%}".format(percent_AM)
    percent_PM = number_PM/squirrels.count()
    percent_PM = "{:.2%}".format(percent_PM)
    number_Adult = squirrels.filter(Age = 'Adult').count()
    number_Juvenile = squirrels.filter(Age = 'Juvenile').count()
    number_Unknown = squirrels.filter(Age = '').count()
    total_n = number_Adult + number_Juvenile + number_Unknown
    percent_Adult = number_Adult/total_n
    percent_Adult = "{:.2%}".format(percent_Adult)
    percent_Juvenile = number_Juvenile/total_n
    percent_Juvenile = "{:.2%}".format(percent_Juvenile)
    percent_Unknown = number_Unknown/total_n
    percent_Unknown = "{:.2%}".format(percent_Unknown)
    number_Gray = squirrels.filter(Primary_Fur_Color = 'Gray').count()
    number_Cinnamon = squirrels.filter(Primary_Fur_Color = 'Cinnamon').count()
    number_Black = squirrels.filter(Primary_Fur_Color = 'Black').count()
    number_Unknown2 = squirrels.filter(Primary_Fur_Color = '').count()
    total_m = number_Gray + number_Cinnamon + number_Black + number_Unknown2
    percent_Gray = number_Gray/total_m
    percent_Gray = "{:.2%}".format(percent_Gray)
    percent_Cinnamon = number_Cinnamon/total_m
    percent_Cinnamon = "{:.2%}".format(percent_Cinnamon)
    percent_Black = number_Black/total_m
    percent_Black = "{:.2%}".format(percent_Black)
    percent_Unknown2 = number_Unknown2/total_m
    percent_Unknown2 = "{:.2%}".format(percent_Unknown2)
    number_Running = squirrels.filter(Running = True).count()
    number_not_Running = squirrels.filter(Running = False).count()
    number_Chasing = squirrels.filter(Chasing = True).count()
    number_not_Chasing = squirrels.filter(Chasing = False).count()
    number_Climbing = squirrels.filter(Climbing = True).count()
    number_not_Climbing = squirrels.filter(Climbing = False).count()
    number_Eating = squirrels.filter(Eating = True).count()
    number_not_Eating = squirrels.filter(Eating = False).count()
    number_Foraging = squirrels.filter(Foraging = True).count()
    number_not_Foraging = squirrels.filter(Foraging = False).count()
    number_Approaches = squirrels.filter(Approaches = True).count()
    number_not_Approaches = squirrels.filter(Approaches = False).count()
    number_Indifferent = squirrels.filter(Indifferent = True).count()
    number_not_Indifferent = squirrels.filter(Indifferent = False).count()
    number_Runs_from = squirrels.filter(Runs_from = True).count()
    number_not_Runs_from = squirrels.filter(Runs_from = False).count()
    context = {
            'Total':total,
            'Morning':number_AM,
            'Night':number_PM,
            'Morning_Percent':percent_AM,
            'Night_Percent':percent_PM,
            'Adult_Number':number_Adult,
            'Juvenile_Number':number_Juvenile,
            'Number_Unknown':number_Unknown,
            'Adult_Percent':percent_Adult,
            'Juvenile_Percent':percent_Juvenile,
            'Unknown_Percent':percent_Unknown,
            'Gray_Number':number_Gray,
            'Cinnamon_Number':number_Cinnamon,
            'Black_Number':number_Black,
            'Number_Unknown2':number_Unknown2,
            'Gray_Percent':percent_Gray,
            'Cinnamon_Percent':percent_Cinnamon,
            'Black_Percent':percent_Black,
            'Unknown2_Percent':percent_Unknown2,
            'Running_Number':number_Running,
            'Chasing_Number':number_Chasing,
            'Climbing_Number':number_Climbing,
            'Eating_Number':number_Eating,
            'Foraging_Number':number_Foraging,
            'Approaches_Number':number_Approaches,
            'Indifferent_Number':number_Indifferent,
            'Runs_from_Number':number_Runs_from,
            'Running_not_Number':number_not_Running,
            'Chasing_not_Number':number_not_Chasing,
            'Climbing_not_Number':number_not_Climbing,
            'Eating_not_Number':number_not_Eating,
            'Foraging_not_Number':number_not_Foraging,
            'Approaches_not_Number':number_not_Approaches,
            'Indifferent_not_Number':number_not_Indifferent,
            'Runs_from_not_Number':number_not_Runs_from
            }
    return render(request, 'squtracker/stats.html',{'context':context})

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

