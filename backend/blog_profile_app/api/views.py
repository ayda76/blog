
from rest_framework import generics, viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from django.db.models import Q
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action

from datetime import datetime, timedelta, date
from rest_framework.response import Response

from ..models import Profile
from .serializers import ProfileSerializer




class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class=None
    my_tags = ["Profile"]
    
    def perform_create(self,serializer):
        user=self.request.user
        profile_instance=serializer.save()
        profile_instance.user=user
        profile_instance.save()
        return Response(profile_instance)
