from django.shortcuts import render, redirect
from .forms import *
from .detect import *
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST': 
        form = RoadForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            road_image = ('media/images/' + str(form.cleaned_data['road_image']))
            name = main(road_image)
            return success(request, name) 
    else: 
        form = RoadForm() 
    return render(request, 'index.html', {'form' : form}) 

def success(request, name): 
    road_image_url = '/media/images/' + name
    road = {'name' : name, 'road_image_url': road_image_url}
    return render(request, 'display.html', {'road' : road}) 