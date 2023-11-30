from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
     name=serializers.CharField(max_length=100)
     roll=serializers.IntegerField()
     city=serializers.CharField(max_length=150)


#to create data 
     def create(self,validated_data):
          return Student.objects.create(**validated_data)
