from rest_framework import serializers
from .models import Student, PersonalInformation, FamilyInformation, EducationInformation
from course.serializers import CourseSerializer
from course.models import Course

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
    course = CourseSerializer(many=True, required = False)

    class Meta:
        model = EducationInformation
        fields = '__all__'

    def create(self, validated_data):
        courses_data = validated_data.pop('course', [])
        education_information = EducationInformation.objects.create(**validated_data)
        for course_data in courses_data:
            Course.objects.create(education_information_id=education_information, **course_data)
        return education_information


class StudentSerializer(serializers.ModelSerializer):
    personal_information = PersonalInformationSerializer()
    family_information = FamilyInformationSerializer()
    education_information = EducationInformationSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        print(f"validated data : {validated_data}")
        personal_information_data = validated_data.pop('personal_information')
        family_information_data = validated_data.pop('family_information')
        education_information_data = validated_data.pop('education_information')

        student = Student.objects.create(**validated_data)
        print(f"education data : {education_information_data}")

        PersonalInformation.objects.create(student_id=student, **personal_information_data)
        FamilyInformation.objects.create(student_id=student, **family_information_data)
        EducationInformation.objects.create(student_id=student, **education_information_data)

        return student