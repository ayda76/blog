from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path , include ,re_path

from .views import (PostViewSet,CommentViewSet)

router = DefaultRouter()
router.register("Post", PostViewSet)
router.register("Comment", CommentViewSet)



urlpatterns = [

    path("", include(router.urls)),
  


]