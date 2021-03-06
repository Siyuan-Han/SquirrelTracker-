from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

app_name ='squtracker'

urlpatterns = [
        path('',views.mainpage),
        path('map/',views.get_map),
        path('sightings/',views.get_sightings),
        path('sightings/stats/',views.get_stats),
        path('sightings/add/',views.addsqu),
        path('sightings/<Unique_squirrel_ID>/', views.updatesqu),
    ]
urlpatterns += staticfiles_urlpatterns()
