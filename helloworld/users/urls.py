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
from django.urls import path,include
from rest_framework import routers

from users import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from users.views import PostViewSet
from users.views import UserModelView

router =routers.DefaultRouter()
router.register("posts",PostViewSet)
router.register("friends",views.FriendsModelViewSet,basename="Friends")
router.register("notifications",views.NotificationModelViewSet,basename="Notifications")
router.register("messages",views.MessageModelViewSet,basename="Messages")
router.register("payment",views.PaymentModelView,basename="Payment")
router.register("users",views.UserModelViewSet,basename="Users")
router.register("user",UserModelView)


urlpatterns = [

    path('',include(router.urls)),
]
