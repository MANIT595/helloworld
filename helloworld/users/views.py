from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render
from django.template.context_processors import request

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *

class FriendsModelViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer
class PaymentModelView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class NotificationModelViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer

class MessageModelViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    def post(self,request,*args, **kwargs):
        title = request.data['title']
        cover = request.data['cover']
        Post.objects.create(title=title,cover=cover)
        return HttpResponse({'message':'Img Uploaded'},status=200)

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UserModelView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerial
    def retrieve(self, request, *args, **kwargs):
        name = self.request.query_params.get('name')
        Users.objects.filter(name=name)
        return HttpResponse({'message':'User Uploaded'},status=200)

