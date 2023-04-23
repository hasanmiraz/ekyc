from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def testview(request):
    if request.method == "GET":
        data = {
            'test':'test'
        }
        return Response(data)