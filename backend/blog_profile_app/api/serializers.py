from rest_framework import serializers
from blog_profile_app.models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email"]

class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model= Profile
        fields=['id','user','firstname','lastname','email']
    
    
    
        
    