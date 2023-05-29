from django.db import models
from student.models import EducationInformation

# Create your models here.

class Course(models.Model):
    education_information_id = models.ForeignKey(EducationInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    university_name = models.CharField(max_length=50)
    code = models.IntegerField(default=0)


class Grade(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)
    semester = models.IntegerField()
