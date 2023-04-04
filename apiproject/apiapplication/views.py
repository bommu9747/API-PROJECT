from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Log,Student
from apiapplication.serializers import LoginStudentSerializer,StudentRegisterSerializer

# Create your views here.


class StudentRegisterAPIView(GenericAPIView):
    serializer_class = StudentRegisterSerializer
    serializer_class_login = LoginStudentSerializer
    def post(self,request):

        login_id=''
        name = request.data.get('name')
        email=request.data.get('email')
        phonenumber=request.data.get('phonenumber')
        pincode=request.data.get('pincode')
        place=request.data.get('place')
        post=request.data.get('post')
        password=request.data.get('password')
        role =request.data.get('role')
        if(Log.objects.filter(username=email)):
            return Response({'messages':'Duplicate email Found!'},status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login= self.serializer_class_login(data={'username':email,'password':password,'role':role})
        
        if serializer_login.is_valid():
            log = serializer_login.save()
            login_id=log.id
            print(login_id)
        serializer =self.serializer_class(data={'name':name,'email':email,'phonenumber':phonenumber,'place':place,'post':post,'pincode':pincode,'password':password,'log_id':login_id,'role':role})

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'student registerers successfully','success':1},status= status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'messages':'Failed','success':0},status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):
    serializer_class =LoginStudentSerializer
    def post(self,request):
        username =request.data.get('username')
        password=request.data.get('password')
        logreg =Log.objects.filter(username=username,password=password)
        if (logreg.count()>0):
            read_serializer=LoginStudentSerializer(logreg,many=True)
            for i in read_serializer.data:
                id=i['id']
            return Response({'data':read_serializer.data,'success':1,'message':'Logged in successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'data':'username or password is invalid' },status = status.HTTP_400_BAD_REQUEST)
class get_studentAPIView(GenericAPIView):
    serializer_class=StudentRegisterSerializer
    def get(self,request):
        queryset=Student.objects.all()
        if(queryset.count()>0):
            serializer=StudentRegisterSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'data get','success':1})
        else:
            return Response({'data':'no data avilable'},status=status.HTTP_400_BAD_REQUEST)

class update_studentAPIView(GenericAPIView):
    serializer_class=StudentRegisterSerializer
    def put(self,request,id):
        queryset=Student.objects.get(pk=id)
        print(queryset)
        serializer=StudentRegisterSerializer(instance=queryset,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated successfully','success':1},status=status.HTTP_200_OK)

class delete_studentAPIView(GenericAPIView):
    def delete(self,request,id):
        delmember=Student.objects.get(pk=id)
        delmember.delete()
        return Response({'messages':'Deleted successful'})
class singleStudentAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=Student.objects.get(pk=id)
        serializer=StudentRegisterSerializer(queryset)
        return Response(serializer.data)



