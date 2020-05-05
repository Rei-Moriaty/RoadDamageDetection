# forms.py 
from django import forms 
from .models import *
  
class RoadForm(forms.ModelForm): 
    class Meta: 
        model = Road 
        fields = ['name', 'road_image'] 