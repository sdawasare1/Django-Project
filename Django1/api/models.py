from pyexpat import model
import re
from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    token = models.IntegerField()

 