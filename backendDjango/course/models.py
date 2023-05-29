from django.db import models
from student.models import EducationInformation

# Create your models here.

class Course(models.Model):
    education_id = models.ForeignKey(EducationInformation, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    course_grade = models.CharField(max_length=50)