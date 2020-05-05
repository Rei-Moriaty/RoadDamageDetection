from django.db import models

# Create your models here.
# models.py 
class Road(models.Model): 
    name = models.CharField(max_length=50) 
    road_image = models.ImageField(upload_to='images/') 