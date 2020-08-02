# forms.py 
from django import forms 
from .models import *
  
class RoadForm(forms.ModelForm): 
    class Meta: 
        model = Road 
        fields = ['name', 'location', 'road_image',] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Textarea(attrs={'class': 'form-control', 'style' : 'resize: none'}),
            'road_image' : forms.FileInput(attrs={'class' : 'custom-file-input'})
        }
    