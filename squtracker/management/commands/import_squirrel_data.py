import csv

from django.core.management import BaseCommand
from squtracker.models import Squirrel
import argparse

from distutils.util import strtobool

class Command(BaseCommand):
        help = 'Please Load squirrel indomation into the database'
            
        def add_arguments(self,parser):
            parser.add_argument('path', type=str)

        def handle(self, *args, **kwargs):
            Squirrel.objects.all().delete()
            path = kwargs['path']
            with open(path, 'rt') as f:
                reader = csv.DictReader(f)
                data = list(reader)
                for row in data:
                    squirrel = Squirrel(
                            X=row['X'],
                            Y=row['Y'],
                            Unique_squirrel_ID=row['Unique Squirrel ID'],
                            Shift=row['Shift'],
                            Date=row['Date'][4:8]+'-'+row['Date'][0:2]+'-'+row['Date'][2:4],
                            Age=row['Age'],
                            Primary_Fur_Color=row['Primary Fur Color'],
                            Location=row['Location'],
                            Specific_Location=row['Specific Location'],
                            Running=strtobool(row['Running']),
                            Chasing=strtobool(row['Chasing']),
                            Climbing=strtobool(row['Climbing']),
                            Eating=strtobool(row['Eating']),
                            Foraging=strtobool(row['Foraging']),
                            Other_Activities=row['Other Activities'],
                            Kuks=strtobool(row['Kuks']),
                            Quaas=strtobool(row['Quaas']),
                            Moans=strtobool(row['Moans']),
                            Tail_flags=strtobool(row['Tail flags']),
                            Tail_twitching=strtobool(row['Tail twitches']),
                            Approaches=strtobool(row['Approaches']),
                            Indifferent=strtobool(row['Indifferent']),
                            Runs_from=strtobool(row['Runs from']),
                            )
                    squirrel.save()
