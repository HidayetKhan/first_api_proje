from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
# function based api view
#THIS IS FOR GET
# @api_view()
# def hello_world(request):
#     return Response({"MSG":"rESPONSE"})

#THIS IS FOR POST and GET at same time
@api_view(['GET','POST'])
def hello_world(request):
    if request.method=='GET':
       return Response({'msg':'meaasge get it'})
    
    if request.method=='POST':
      print(request.data)
      return Response({"MSG":"thi data is post",'data':request.data})

