from django.forms import ModelForm
from .models import Squirrel


class SquForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__' 
