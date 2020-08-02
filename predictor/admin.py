from django.contrib import admin
from .models import *
from django.utils.html import format_html

class RoadAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'road_image_func', 'road_image_predicted_func', 'priority', 'work_status']
    ordering = ['name']
    def road_image_func(self, instance):
        address = '/media/' + str(instance.road_image)
        return format_html('<a href="%s" target="_blank"><img src="%s" width="300" height="300" /></ad>' % (address, address))
    def road_image_predicted_func(self, instance):
        address = '/media/' + str(instance.road_image_predicted)
        return format_html('<a href="%s" target="_blank"><img src="%s" width="300" height="300" /></a>' % (address, address))

# Register your models here.
admin.site.site_header = "BBMP"
admin.site.register(Road, RoadAdmin)