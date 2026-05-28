import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from tests.factories import UserFactory
from tests.factories_profile import ProfileFactory

from django.contrib.auth.models import User
from blog_profile_app.models import Profile
from tests.integrationtest.post_tests.test_post_creation import get_tokens_for_user

@pytest.mark.django_db
def test_password_change_success():

    client = APIClient()

    user = User.objects.create_user(
        username='testuser',
        password='OldPass123'
    )

    profile = Profile.objects.create(
        user=user
    )

    token = get_tokens_for_user(user)

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    response = client.post(
        '/profile/change/password/',
        {
            "old_password": "OldPass123",
            "new_password1": "NewStrongPass123",
            "new_password2": "NewStrongPass123"
        }
    )

    assert response.status_code == 200

    user.refresh_from_db()

    assert user.check_password(
        "NewStrongPass123"
    )
    
@pytest.mark.django_db
def test_password_change_wrong_old_password():

    client = APIClient()

    user = User.objects.create_user(
        username='testuser',
        password='OldPass123'
    )

    profile = Profile.objects.create(
        user=user
    )

    token = get_tokens_for_user(user)

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    response = client.post(
        '/profile/change/password/',
        {
            "old_password": "OldPass",
            "new_password1": "NewStrongPass123",
            "new_password2": "NewStrongPass123"
        }
    )

    assert response.status_code == 400

@pytest.mark.django_db
def test_password_change_password_mismatch():

    client = APIClient()

    user = User.objects.create_user(
        username='testuser',
        password='OldPass123'
    )

    profile = Profile.objects.create(
        user=user
    )

    token = get_tokens_for_user(user)

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    response = client.post(
        '/profile/change/password/',
        {
            "old_password": "OldPass123",
            "new_password1": "NewStrongPass123",
            "new_password2": "NewStrongPass"
        }
    )

    assert response.status_code == 400
  
@pytest.mark.django_db 
def test_password_change_without_login():
    client = APIClient()

    user = User.objects.create_user(
        username='testuser',
        password='OldPass123'
    )

    profile = Profile.objects.create(
        user=user
    )


    response = client.post(
        '/profile/change/password/',
        {
            "old_password": "OldPass123",
            "new_password1": "NewStrongPass123",
            "new_password2": "NewStrongPass"
        }
    )

    assert response.status_code == 401 