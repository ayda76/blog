from blog_profile_app.api.serializers import ProfileSerializer
import pytest
from tests.factories_profile import UserFactory
from tests.factories_profile import ProfileFactory
from faker import Faker
fake=Faker()


@pytest.mark.django_db
class TestProfileSerializer():
    

    def test_serializer_output(self):    
        profile=ProfileFactory()
        serializer_data=ProfileSerializer(profile).data
        
        assert serializer_data['email'] == 'test@test.com'
        assert serializer_data['user'] is not None
        assert serializer_data['user']['username'] == profile.user.username
        
    def test_partial_update(self):
        profile=ProfileFactory()
        serializer=ProfileSerializer(profile,data={'firstname':'sara'},partial=True)
        assert serializer.is_valid()
        updated_profile=serializer.save()
        assert updated_profile.firstname == 'sara'
        
    def test_invalid_partial_update(self):
        profile=ProfileFactory()
        serializer=ProfileSerializer(profile,data={'email':30},partial=True)
     
        assert  serializer.is_valid() == False
        print(f"serializer errors:::{serializer.errors}")
        assert 'email' in serializer.errors