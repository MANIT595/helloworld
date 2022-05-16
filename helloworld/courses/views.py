from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import *
from .serializers import *

# Create your views here.
class Courseslist(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class CartModelViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class BcoursesModelViewSet(viewsets.ModelViewSet):
    queryset = Boughtcourses.objects.all()
    serializer_class = BoughtcoursesSerializer

class CoursesPostlist(GenericAPIView, CreateModelMixin):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    def post(self, request):
        return self.create(request)


class CoursesInlist(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)
    def put(self, request, **kwargs):
        return self.update(request, **kwargs)
    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)


class CoursesUpdatelist(GenericAPIView, UpdateModelMixin):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)
    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)


class CoursesDeletelist(GenericAPIView, DestroyModelMixin):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)
