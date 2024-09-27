from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    department=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    salary=models.IntegerField(max_length=100)