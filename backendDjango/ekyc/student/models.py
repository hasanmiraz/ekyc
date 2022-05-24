from django.db import models
from django.forms import DateField

# Create your models here.

class student (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.CharField(DateField)
    phone_number = models.IntegerField()
    