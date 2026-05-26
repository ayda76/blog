
from rest_framework import generics, viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from django.db.models import Q
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, NotFound
from datetime import datetime, timedelta, date
from rest_framework.response import Response

from .services import add_profile
from blog_profile_app.models import Profile
from ..models import (Post,Comment)
from .serializers import (PostSimpleSerializer,
                          CommentSimpleSerializer,
                          PostGetSerializer,
                          CommentGetSerializer)




class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    pagination_class=None
    my_tags = ["Post"]
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT','PATCH']:
            return PostSimpleSerializer
        else:
            return PostGetSerializer
        
    def perform_create(self, serializer):
        instance=add_profile(self,serializer)
        return instance
        
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    pagination_class=None
    my_tags = ["Post"]
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT','PATCH']:
            return CommentSimpleSerializer
        else:
            return CommentGetSerializer
        
    def perform_create(self, serializer):
        instance=add_profile(self,serializer)
        return instance
        
    