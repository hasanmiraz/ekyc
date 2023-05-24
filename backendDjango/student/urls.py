from django.urls import path
from . import views

urlpatterns = [
    path("testpathstudent", views.testview),
    path("student", views.StudentView),
]