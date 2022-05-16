from django.db import models

# Create your models here.


class Courses(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)
    desc = models.CharField(default=None,max_length=400)
    price = models.IntegerField(default=None)

class Cart(models.Model):
    name = models.CharField(max_length=400,unique=True)
    desc = models.CharField(default=None,max_length=400)
    price = models.IntegerField(default=None)

class Boughtcourses(models.Model):
    name = models.CharField(max_length=400,unique=True)
    desc = models.CharField(default=None,max_length=400)
    price = models.IntegerField(default=None)