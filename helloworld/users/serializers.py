from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from .models import *

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','cover']

class UsersSerial(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name','email']