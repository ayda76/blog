from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path , include ,re_path
from .views import ProfileViewSet 

router = DefaultRouter()
router.register("Profile", ProfileViewSet)



urlpatterns = [

    path("", include(router.urls)),

]