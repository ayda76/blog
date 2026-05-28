import pytest
from rest_framework.test import APIClient
from tests.factories_profile import ProfileFactory
from tests.factories_post import PostFactory
from tests.integrationtest.post_tests.test_post_creation import get_tokens_for_user
from blog_post_app.models import (Post,StatusPost)

# SUCCESS TESTS
@pytest.mark.django_db
def test_post_delete_with_jwt_auth():
    
    client=APIClient()
    
    profile=ProfileFactory()
    user=profile.user
    post=PostFactory(profile_related=profile)
    token=get_tokens_for_user(user)
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    
    response=client.delete(f'/post/Post/{post.id}/')
    
    assert response.status_code == 204
    
    assert Post.objects.count() == 0
    
# AUTH TESTS
@pytest.mark.django_db
def test_post_delete_not_login():
    
    client=APIClient()
    
    post=PostFactory()
    
    response=client.delete(f'/post/Post/{post.id}/')
    
    assert response.status_code == 401
    
    assert Post.objects.count() == 1
    
@pytest.mark.django_db
def test_post_delete_with_invalid_token():
    
    client=APIClient()

    post=PostFactory()
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer invalid token")
    
    response=client.delete(f'/post/Post/{post.id}/')
    
    assert response.status_code == 401
    
    assert Post.objects.count() == 1
    
@pytest.mark.django_db
def test_post_delete_with_wrong_profile():
    
    client=APIClient()

    profile_owner=ProfileFactory()
    profile_strenger=ProfileFactory()
    post=PostFactory(profile_related=profile_owner)
    token=get_tokens_for_user(profile_strenger.user)
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    
    response=client.delete(f'/post/Post/{post.id}/')
    
    assert response.status_code == 401
    
    assert Post.objects.count() == 1