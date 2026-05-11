from tests.factories_profile import ProfileFactory
import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestProfileModel:
    def test_profile_creation(self):
        profile=ProfileFactory()
        assert profile.id is not None
        
    def test_profile_str(self):
        profile=ProfileFactory()
        assert str(profile) ==profile.user.username
