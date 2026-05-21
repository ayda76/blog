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
        
    def validate(self, attrs):

        request = self.context.get('request')

        if not request:
            return attrs

        user = request.user

        if not self.instance:

            if Profile.objects.filter(
                user=user
            ).exists():

                raise serializers.ValidationError(
                    'this user already has a profile'
                )

        return attrs
    
    
    
        
    