from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class PersonalInformation(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True, related_name='personal_information')
    dob = models.DateField(null=True)
    bloodGroup = models.CharField(max_length=10)
    
class FamilyInformation(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True, related_name='family_information')
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    siblings = models.IntegerField()

class EducationInformation(models.Model):
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True, related_name='education_information')
    status = models.CharField(max_length=50)
    university_name = models.CharField(max_length=50)
    
    