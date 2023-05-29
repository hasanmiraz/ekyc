from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class PersonalInformation(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True)
    dob = models.DateField()
    bloodGroup = models.CharField(max_length=10)
    
class FamilyInformation(models.Model):
    studnt_id = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    siblings = models.IntegerField()

class EducationInformation(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True)
    status = models.CharField(max_length=50)
    
    