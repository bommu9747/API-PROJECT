from django.db import models

# Create your models here.
class Log(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20,unique=True)
    role = models.CharField(max_length=10)
    def __str__(self):
        return self.username
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    log_id =models.OneToOneField(Log,on_delete=models.CASCADE)
    role=models.CharField(max_length=10)
    def __str__(self):
        return self.name