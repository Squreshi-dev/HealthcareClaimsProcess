from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Patient

def home(request,*args, **kwargs):
    data = {
        "text": "Hello World"
    }
    return JsonResponse(data)


#saving patient information

@api_view(['POST'])
def insert_Patient_Record(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data="Data has been inserted", status=201)
    return Response(data="Error in saving data", status=400)


@api_view(['GET'])
def retrieve_Patient_Records(request):
    items = Patient.objects.all()
    print(items)
    
    serializer = PatientSerializer(data = list(items), many=True)
    
    if serializer.is_valid():
        return Response(data=serializer.data, status=200)
    print(serializer.data)
    return Response(data="Error in retirving data data", status=400)
    




#Retrive all the patient information