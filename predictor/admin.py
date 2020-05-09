from django.contrib import admin
from .models import *


class RoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'road_image', 'road_image_predicted')
# Register your models here.
admin.site.register(Road, RoadAdmin)