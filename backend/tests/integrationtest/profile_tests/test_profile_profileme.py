import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from tests.factories import UserFactory
from tests.factories_profile import ProfileFactory

from django.contrib.auth.models import User
from blog_profile_app.models import Profile
from tests.integrationtest.post_tests.test_post_creation import get_tokens_for_user


@pytest.mark.django_db
def test_profile_me_authenticated():

    client = APIClient()

    profile = ProfileFactory()

    token = get_tokens_for_user(profile.user)

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    response = client.get(
        '/profile/ME/'
    )

    assert response.status_code == 200

    assert response.data["id"] == profile.id
    
@pytest.mark.django_db    
def test_profile_me_without_login():

    client = APIClient()

    response = client.get(
        '/profile/ME/'
    )

    assert response.status_code == 401

    