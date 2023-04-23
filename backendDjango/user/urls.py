from django.urls import path
from . import views

urlpatterns = [
    path("testpathuser", views.testview)
]