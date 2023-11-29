from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# model object singal student data
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render( serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data)we can use this to reduce the line of code

#query set all studet daat
def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    json_data=JSONRenderer().render( serializer.data)
    return HttpResponse(json_data,content_type='application/json')