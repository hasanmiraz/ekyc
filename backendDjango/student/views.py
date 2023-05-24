from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

@api_view(["GET"])
def testview(request):
    if request.method == "GET":
        data = {
            'test':'test'
        }
        return Response(data)
    
@api_view(["GET","POST"])
def StudentView(request):
    if request.method == "GET":
        quryset = Student.objects.all()
        serializer = StudentSerializer(quryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)