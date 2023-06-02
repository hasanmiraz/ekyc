from rest_framework import serializers
from .models import Course, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    # grades = GradeSerializer(many = True)
    education_information_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

    # def create(self, validated_data):
    #     grades_data = validated_data.pop('grades', [])
    #     print(f"grade data : {grade_data}")
    #     course = Course.objects.create(**validated_data)
    #     for grade_data in grades_data:
    #         Grade.objects.create(course_id = course, **grade_data)
    #     return course