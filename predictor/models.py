from django.db import models

# Create your models here.
# models.py 
class Road(models.Model): 
    priority_choices = [("L", "Low"), ("H", "High")]
    work_status_choices = [("1","Yet to begin"), ("2", "On Progress"), ("3", "Completed")]
    name = models.CharField(max_length=50)
    location = models.TextField(default=None) 
    road_image = models.ImageField(upload_to='images/')
    road_image_predicted = models.ImageField(upload_to='images/', default= None) 
    priority = models.TextField(choices = priority_choices, default="low")
    work_status = models.TextField(choices = work_status_choices, default="Yet to begin")