from django.db import models

# Create your models here.
class Bike(models.Model):
    brand_name=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.IntegerField()
    price=models.IntegerField()
    
    
