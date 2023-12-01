from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
#FUNCTION BASED API
# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request):#yha ek or argument denge pk=None
#     if request.method=='GET':
#         id=request.data.get('id')
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data is posted'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     if request.method=='PUT':
#         #yha per id=pk likhnese browser pe data show hoga
#         id=request.data.get('id')
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data is put'})
#         return Response(serializer.errors)
    
#     if request.method=='DELETE':
#         id=request.data.get('id')
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'data is deleted'})

#CLASSED BAISED API
class StudentAPI(APIView):
    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is posted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    