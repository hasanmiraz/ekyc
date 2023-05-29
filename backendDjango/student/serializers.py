from rest_framework import serializers
from .models import Student, PersonalInformation, FamilyInformation, EducationInformation
from course.serializers import CourseSerializer

class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = '__all__'

class FamilyInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyInformation
        fields = '__all__'

class EducationInformationSerializer(serializers.ModelSerializer):
    course = CourseSerializer(source='course_set', many=True, read_only=True)

    class Meta:
        model = EducationInformation
        fields = '__all__'        

class StudentSerializer(serializers.ModelSerializer):
    personal_information = PersonalInformationSerializer(source="personalinformation_set", many = True, read_only = True)
    family_information = FamilyInformationSerializer(source="familyinformation_set", many = True, read_only = True)
    education_information = EducationInformationSerializer(source="educationinformation_set", many = True, read_only = True)

    class Meta:
        model = Student
        fields = '__all__'
