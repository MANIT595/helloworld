from rest_framework import serializers
from .models import *


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
class BoughtcoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boughtcourses
        fields = '__all__'
