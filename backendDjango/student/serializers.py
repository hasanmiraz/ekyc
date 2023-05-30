from rest_framework import serializers
from .models import Student, PersonalInformation, FamilyInformation, EducationInformation
from course.serializers import CourseSerializer

class PersonalInformationSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PersonalInformation
        fields = '__all__'

class FamilyInformationSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FamilyInformation
        fields = '__all__'

class EducationInformationSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(read_only=True)
    course = CourseSerializer(source='course_set', many=True, read_only=True)

    class Meta:
        model = EducationInformation
        fields = '__all__'        

class StudentSerializer(serializers.ModelSerializer):
    personal_information = PersonalInformationSerializer()
    family_information = FamilyInformationSerializer()
    education_information = EducationInformationSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        personal_information_data = validated_data.pop('personal_information')
        family_information_data = validated_data.pop('family_information')
        education_information_data = validated_data.pop('education_information')

        student = Student.objects.create(**validated_data)

        PersonalInformation.objects.create(student_id=student, **personal_information_data)
        FamilyInformation.objects.create(student_id=student, **family_information_data)
        EducationInformation.objects.create(student_id=student, **education_information_data)

        return student