from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

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
    


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn’t match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)
    
    

        
class ProfileMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


    
    
        
    