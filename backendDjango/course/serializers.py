from rest_framework import serializers
from .models import Course, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    education_information_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'