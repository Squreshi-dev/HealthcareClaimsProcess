
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('patient/create/', views.insert_Patient_Record),
    path('patient/all/', views.retrieve_Patient_Records),
]