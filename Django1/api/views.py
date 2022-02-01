# from turtle import st
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from api.models import Student
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.



def Student_detail(request):
    stu = Student.objects.get(id=1)
    serializer =  StudentSerializers(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')