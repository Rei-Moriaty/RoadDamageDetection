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
            return success(request, name, str(form.cleaned_data['road_image'])) 

    else: 
        form = RoadForm() 
    return render(request, 'index.html', {'form' : form}) 

def success(request, new_name, old_name): 
    road_image_url = '/media/images/' + new_name
    old_name = 'images/' + old_name
    print(old_name)
    r = Road.objects.get(road_image = old_name)
    r.road_image_predicted = 'images/' + new_name
    r.save()
    road = {'name' : new_name, 'road_image_url': road_image_url}
    return render(request, 'display.html', {'road' : road}) 