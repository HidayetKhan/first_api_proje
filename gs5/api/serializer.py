from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(read_only=True)
    class meta:
        model=Student
        feild=['id','name','roll','city']
        #you can use this also
        #read_only=['name']
        #or extra_kwargs={'name':{'read_only':True}}

# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=150)

#     #to create first add method in serializer class
#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)
    
#     #to update a data 
#     def update(self,instance,validated_data):
#         print(instance.name)
#         instance.name=validated_data.get('name',instance.name)
#         print(instance.name)
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance