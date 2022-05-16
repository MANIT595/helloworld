from django.contrib.auth.models import AbstractUser
from django.db import models

#rm db.sqllite3 -- to remove total data
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dob = models.DateField(default=None)
    gender = models.CharField(max_length=2)
    address = models.CharField(max_length=40000,default=None)
    country = models.CharField(max_length=100,default="India")

def upload_path(instance,filname):
    return '/'.join(['covers',str(instance.title),filname])

class Post(models.Model):
    title = models.CharField(max_length=40,blank=False)
    cover = models.ImageField(blank=True,null=True,upload_to=upload_path)
class Payment(models.Model):
    pay1 = models.AutoField(primary_key=True)
    cardnumber =models.IntegerField(max_length=16)
    cvv =models.IntegerField(max_length=3)
    mm=models.IntegerField(max_length=2)
    yy=models.IntegerField(max_length=2)
    name=models.CharField(max_length=40,default=None)
class Friends(models.Model):
    f1 = models.ForeignKey(Users, related_name='friend1',on_delete=models.CASCADE)
    f2 = models.ForeignKey(Users, related_name='friend2',on_delete=models.CASCADE)
    status = models.IntegerField(default=None)
class Subjects(models.Model):
    Sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400)
    desc = models.CharField(max_length=400)
    price = models.IntegerField(default=None)
class Messages(models.Model):
    fm1 = models.ForeignKey(Users, related_name='mf1',on_delete=models.CASCADE)
    fm2 = models.ForeignKey(Users, related_name='mf2',on_delete=models.CASCADE)
    messages = models.CharField(max_length=400000,default=None)
class Notification(models.Model):
    name = models.CharField(max_length=10,default="Admin")
    notifications = models.CharField(max_length=400000,default=None)





