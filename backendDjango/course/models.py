from django.db import models

# Create your models here.

class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_grade = models.CharField(max_length=50)