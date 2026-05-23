from django.db.models import Q
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
# from datetime import datetime, timedelta, date
from rest_framework import generics, viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import PasswordChangeForm
from drf_yasg.utils import swagger_auto_schema 
from rest_framework.decorators import action

from ..models import Profile
from .serializers import *


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


# Helper function to generate JWT token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(APIView):
    my_tags = ["Profile"]
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = get_tokens_for_user(user)  # Generate JWT tokens for user
            Profile.objects.get_or_create(user=user)  # create profile
            return Response(tokens, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    my_tags = ["Profile"]
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                tokens = get_tokens_for_user(user)  
                return Response(tokens, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                                  
                                  

class ProfileMeViewSet(generics.ListAPIView):
    
    my_tags = ["Profile"]
    serializer_class = ProfileMeSerializer
    pagination_class=None
    
    def get(self,request):
        
        profileSelected = Profile.get_user_jwt( self,request )
        serializer = ProfileMeSerializer(profileSelected)
        return Response(serializer.data)
        
class PasswordChangeView(APIView):
    my_tags = ["Profile"]

    @swagger_auto_schema(
        request_body=PasswordChangeSerializer,
        responses={
            200: "Password changed successfully",
            400: "Bad Request",
           
        },
    )
    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            userSelecte = Profile.get_user_jwt(self , request).user
            # Validate old and new passwords using Django's PasswordChangeForm
            form = PasswordChangeForm(userSelecte, serializer.validated_data)
            if form.is_valid():
                # Save the new password
                form.save()
                return Response({'success': 'Password changed successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        


       
