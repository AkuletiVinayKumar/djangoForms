from django.db import models
from app.forms import *
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    age = models.IntegerField()
    email = models.EmailField()
    date = models.DateField()
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
