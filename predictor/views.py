from django.shortcuts import render, redirect
from .forms import *
from .detect import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST': 
        form = RoadForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            road_image = ('media/images/' + str(form.cleaned_data['road_image']))
            print(str(form.cleaned_data['road_image']))
            name, count = main(road_image)
            return success(request, name, str(form.cleaned_data['road_image']), count) 

    else: 
        form = RoadForm() 
    return render(request, 'index.html', {'form' : form}) 

def success(request, new_name, old_name, count): 
    road_image_url = '/media/images/' + new_name
    old_name = 'images/' + old_name
    print(old_name)
    r = Road.objects.filter(road_image = old_name).first()
    r.road_image_predicted = 'images/' + new_name
    if(count >2):
        r.priority = "H"
    else:
        r.priority = "L"
    r.work_status = "1"
    print(r.priority)
    print(count)
    r.save()
    road = {'name' : new_name, 'road_image_url': road_image_url}
    return render(request, 'display.html', {'road' : road}) 