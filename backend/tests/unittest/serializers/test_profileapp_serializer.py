from blog_profile_app.api.serializers import ProfileSerializer
import pytest
from tests.factories_profile import UserFactory
from tests.factories_profile import ProfileFactory
from faker import Faker
from rest_framework.test import (
    APIRequestFactory
)
fake=Faker()


@pytest.mark.django_db
class TestProfileSerializer():
    

    def test_serializer_output(self):    
        profile=ProfileFactory()
        serializer_data=ProfileSerializer(profile).data
        
        assert serializer_data['email'] == profile.email
        assert serializer_data['user'] is not None
        assert serializer_data['user']['username'] == profile.user.username
        
    def test_partial_update(self):
        profile=ProfileFactory()
        request=APIRequestFactory().patch('/profile/Profile')
        request.user = profile.user
        serializer=ProfileSerializer(profile,data={'firstname':'sara'},partial=True,context={'request':request})
        assert serializer.is_valid() == True
        updated_profile=serializer.save()
        assert updated_profile.firstname == 'sara'
        
    def test_invalid_partial_update(self):
        profile=ProfileFactory()
        serializer=ProfileSerializer(profile,data={'email':30},partial=True)
     
        assert  serializer.is_valid() == False
        print(f"serializer errors:::{serializer.errors}")
        assert 'email' in serializer.errors
        serializer=ProfileSerializer(profile,data={'email':None},partial=True)
        
        assert  serializer.is_valid() == False
        print(f"serializer errors none email:::{serializer.errors}")
    
    def test_user_already_has_profile(self):
        user=UserFactory()
        profile=ProfileFactory(user=user)
        request=APIRequestFactory().post('/profile/Profile')
        request.user=user
        payload={
            'firstname':'ali',
            'lastname':'abdoli',
            'email':'ex@gmail.com',
            'phone':'091234564657',
            'address':'xxxxxxxxx'
            
        }
        serializer=ProfileSerializer(data=payload,context={'request':request})
        assert  serializer.is_valid() == False
        assert ('non_field_errors' in serializer.errors)
