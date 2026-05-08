from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path , include ,re_path

router = DefaultRouter()
# router.register("Center", CenterViewSet)



urlpatterns = [

    path("", include(router.urls)),
  


]