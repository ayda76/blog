
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

from ..models import (Post,Comment)
from .serializers import (PostSerializer,CommentSerializer)
from blog_profile_app.models import Profile



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class=None
    my_tags = ["Post"]

    def perform_create(self, serializer):
        try:    
            profile_login=Profile.get_user_jwt(self,self.request)
            post_instance=serializer.save(profile_related=profile_login)
            return Response(post_instance)        
        except:
            raise ValidationError({"detail":"login problem"})
        
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class=None
    my_tags = ["Post"]
    def perform_create(self, serializer):
        try:    
            profile_login=Profile.get_user_jwt(self,self.request)
            comment_instance=serializer.save(profile_commented=profile_login)
            return Response(comment_instance)        
        except:
            raise ValidationError({"detail":"login problem"})
    