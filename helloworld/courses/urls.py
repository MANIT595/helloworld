"""Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.db import router
from django.urls import path,include
from courses import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register("cart",views.CartModelViewSet,basename="Cart")
router.register("bcourses",views.BcoursesModelViewSet,basename="Bcourses")

urlpatterns = [
    path('chome/', views.Courseslist.as_view()),
path('c/',include(router.urls)),
    path('cpost/', views.CoursesPostlist.as_view()),
    path('chome/<int:pk>/', views.CoursesInlist.as_view()),
    path('cpost/<int:pk>/', views.CoursesUpdatelist.as_view()),
    path('cdelete/<int:pk>/', views.CoursesDeletelist.as_view()),

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)