from django.db import models

# Create your models here.
# models.py 
class Road(models.Model): 
    name = models.CharField(max_length=50)
    location = models.TextField(default=None) 
    road_image = models.ImageField(upload_to='images/')
    road_image_predicted = models.ImageField(upload_to='images/', default= None) 