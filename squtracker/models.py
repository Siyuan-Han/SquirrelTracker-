from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    X = models.DecimalField(
            help_text = _('Filling in Longitude'),
            max_digits = 20,
            blank = True,
            decimal_places = 15,
            )
    
    Y = models.DecimalField(
            help_text = _('Filling in Latitude'),
            max_digits = 20,
            blank = True,
            decimal_places = 15,)
    
    Unique_squirrel_ID = models.CharField(
            help_text=_('Unique ID for squirrel number'),
            primary_key = True,
            max_length=20,)
    #shiftchoice
    AM = 'AM'
    PM = 'PM'
    TIMEOFDAY = (
            (AM, 'AM'),
            (PM, 'PM'),
        )
    
    Shift = models.CharField(
            help_text=_('Choose from AM or PM'),
            choices = TIMEOFDAY,
            blank = True,
            max_length=20,
        )
    
    Date = models.DateField(
            help_text=_('Filling in date when squirrel was spotted'),
        )

          
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            ) 
    Age = models.CharField(
            help_text=_('Choose age from adult or juvenile'),
            choices = AGE_CHOICES,
            blank = True,
            max_length=20,
        )
    
    GREY= 'Grey'
    CINNAMON= 'Cinnamon'
    BLACK = 'Black'
    FUR_COLOR = (
           (GREY,'Grey'),
           (CINNAMON,'Cinnamon'),
           (BLACK,'Black'),
        )
    Primary_Fur_Color = models.CharField(
            help_text=_('Choose color form gray, cinnamon or black'),
            choices = FUR_COLOR,
            blank = True,
            max_length=20,)
        
    #location choice
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Groud'
    
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION =(
           (GROUND_PLANE,'Ground Plane'),
           (ABOVE_GROUND,'Above Ground'),
           )
        
    Location = models.CharField(
            help_text=_('Choose location from ground plane or above ground'),
            choices = LOCATION,
            blank = True,
            max_length=20,)

    Specific_Location = models.CharField(
            help_text=_('Additional information for the squirrel location'),
            blank = True,
            max_length=20,)

    Running = models.BooleanField(
            help_text=_('Select if squirrel was running'),
            default=False,)

    Chasing = models.BooleanField(
            help_text=_('Select if squirrel was chasing'),
            default=False,)

    Climbing = models.BooleanField(
            help_text=_('Select if squirrel was climbing'),
            default=False,)

    Eating = models.BooleanField(
            help_text=_('Select if squirrel was eating'),
            default=False,)

    Foraging = models.BooleanField(
            help_text=_('Select if squirrel was foraging'),
            default=False,)

    Other_Activities = models.TextField(
            help_text=_('Filling in other activity by squirrel'),
            blank=True,)

    Kuks = models.BooleanField(
            help_text=_('Select if squirrel was kuking'),
            default=False,
        )

    Quaas = models.BooleanField(
            help_text=_('Select if squirrel was quaaing'),
            default=False,
        )

    Moans = models.BooleanField(
            help_text=_('Select if squirrel was moaning'),
            default=False,
        )

    Tail_flags = models.BooleanField(
            help_text=_('Select if squirrel was flagging tail'),
            default=False,
        )

    Tail_twitching = models.BooleanField(
            help_text=_('Select if squirrel was twitching tail'),
            default=False,
        )

    Approaches = models.BooleanField(
        help_text=_('Select if squirrel was approaching human'),
        default=False,
        )

    Indifferent = models.BooleanField(
            help_text=_('Select if squirrel was indifferent to human'),
        default=False,
        )
    Runs_from = models.BooleanField(
            help_text=_('Select if squirrel was running from human'),
            default=False,
        )

    def __str__(self):
        return self.Unique_squirrel_ID
