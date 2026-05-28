import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from tests.factories import UserFactory
from tests.factories_profile import ProfileFactory
from blog_post_app.models import (Post,StatusPost)
from blog_profile_app.models import Profile

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@pytest.mark.django_db
def test_post_creation_with_jwt_auth():
    
    client=APIClient()
    
    profile=ProfileFactory()
    user=profile.user
    
    token=get_tokens_for_user(user)
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    
    response=client.post('/post/Post/',{'title':'test','description':'test post creation with jwt auth'})
    
    assert response.status_code == 201
    
    assert response.data["title"] == "test"
    
    assert Post.objects.count() == 1
    post = Post.objects.first()
    assert post.profile_related == profile
    assert post.status_post == StatusPost.POSTED
    
"""
this test covers
- URL routing
- JWT auth
- permissions
- ViewSet
- serializer
- service layer
- database
- signal
- response generation
"""


@pytest.mark.django_db
def test_post_creation_without_login():
    client=APIClient()
    
    response=client.post('/post/Post/',{'title':'test','description':'test post creation without login'})
    
    assert response.status_code in [401, 403]
    assert Post.objects.count() == 0
    
@pytest.mark.django_db
def test_post_creation_invalid_token():
    client=APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer invalid invalid test token")
    
    response=client.post('/post/Post/',{'title':'test','description':'test post creation with invalid token'})
    
    assert response.status_code == 401
    assert Post.objects.count() == 0


@pytest.mark.django_db
def test_post_creation_with_missing_data():
    
    client=APIClient()
    
    profile=ProfileFactory()
    user=profile.user
    
    token=get_tokens_for_user(user)
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    
    response=client.post('/post/Post/',{'description':'test post creation with missing data'})
    
    assert response.status_code == 400
    
    assert "title" in response.data
    

