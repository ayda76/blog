import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from tests.factories import UserFactory
from tests.factories_profile import ProfileFactory

from django.contrib.auth.models import User
from blog_profile_app.models import Profile




@pytest.mark.django_db
def test_register_success():

    client = APIClient()

    response = client.post(
        '/profile/SignUp/',
        {
            "username": "testuser",
            "password": "StrongPass123",
            "password2": "StrongPass123"
        }
    )

    assert response.status_code == 201

    assert User.objects.count() == 1

    assert Profile.objects.count() == 1

    assert "access" in response.data
    assert "refresh" in response.data
    
"""
in this test we covered these parts:
- serializer validation
- user creation
- profile auto creation
- JWT generation
- response structure
"""

@pytest.mark.django_db
def test_register_duplicate_username():
    client = APIClient()
    
    user=UserFactory()
    
    response = client.post(
        '/profile/SignUp/',
        {
            "username": user.username,
            "password": "StrongPass123",
            "password2": "StrongPass123"
        }
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_register_password_mismatch():
    client = APIClient()

    response = client.post(
        '/profile/SignUp/',
        {
            "username": "testuser",
            "password": "StrongPass12345",
            "password2": "StrongPass123"
        }
    )

    assert response.status_code == 400

    assert User.objects.count() == 0

    assert Profile.objects.count() == 0

    assert "access" not in response.data
    assert "refresh" not in response.data    


# @pytest.mark.django_db
# def test_register_weak_password():
#     client = APIClient()

#     response = client.post(
#         '/profile/SignUp/',
#         {
#             "username": "testuser",
#             "password": "111",
#             "password2": "111"
#         }
#     )

#     assert response.status_code == 400

#     assert User.objects.count() == 0

#     assert Profile.objects.count() == 0

