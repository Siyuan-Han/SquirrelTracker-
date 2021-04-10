from django.core.management.base import BaseCommand

import csv
  
from squtracker.models import Squirrel
class Command(BaseCommand):
        def add_arguments(self, parser):
            parser.add_argument('csv_file')
        def handle(self, *args, **options):
            dict_ = {} 
            s = Squirrel.objects.all()
            with open(options['csv_file'],"w") as fp:
                for i in s:
                    dict_['X'] = i.X
                    dict_['Y'] = i.Y
                    dict_['Shift'] = i.Shift
                    dict_['Date'] = i.Date
                    dict_['Unique Squirrel ID'] = i.Unique_squirrel_ID
                    dict_['Age'] = i.Age
                    dict_['Primary Fur Color'] = i.Primary_Fur_Color
                    dict_['Location'] = i.Location
                    dict_['Specific Location'] = i.Specific_Location
                    dict_['Running'] = i.Running
                    dict_['Chasing'] = i.Chasing
                    dict_['Climbing'] = i.Climbing
                    dict_['Eating'] = i.Eating
                    dict_['Foraging'] = i.Foraging
                    dict_['Other Activities'] = i.Other_Activities
                    dict_['Kuks'] = i.Kuks
                    dict_['Quaas'] = i.Quaas
                    dict_['Moans'] = i.Moans
                    dict_['Tail Flags'] = i.Tail_flags
                    dict_['Tail Twitches'] = i.Tail_twitching
                    dict_['Approaches'] = i.Approaches
                    dict_['Indifferent'] = i.Indifferent
                    dict_['Runs from'] = i.Runs_from
                    writer = csv.DictWriter(fp,delimiter=",",fieldnames=dict_.keys())
                    writer.writeheader()
                    writer.writerow(dict_)
