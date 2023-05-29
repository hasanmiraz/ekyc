from rest_framework import serializers
from .models import Course, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    grade = GradeSerializer(source='grade_set', many= True)
    class Meta:
        model = Course
        fields = '__all__'