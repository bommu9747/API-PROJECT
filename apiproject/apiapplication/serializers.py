from rest_framework import serializers
from .models import Log,Student

class LoginStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def create(self,validated_data):
        return Student.objects.create(**validated_data)