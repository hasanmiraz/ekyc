from rest_framework import serializers
from .models import Student, PersonalInformation

class StudentPersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    studentPersonalInformation = StudentPersonalInformationSerializer(many = True, read_only = True)

    class Meta:
        model = Student
        fields = ('id', 'name', 'studentPersonalInformation')
