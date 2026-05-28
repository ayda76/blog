import pytest
from rest_framework.test import APIClient

from tests.factories_profile import ProfileFactory
from tests.factories_post import PostFactory
from blog_post_app.models import (Post,Comment)
from blog_profile_app.models import Profile
from tests.integrationtest.post_tests.test_post_creation import get_tokens_for_user

# SUCCESS TEST
@pytest.mark.django_db
def test_comment_create_with_jwt():
    client=APIClient()
    
    post=PostFactory()
    profile=ProfileFactory()
    user=profile.user
    
    token=get_tokens_for_user(user)
 
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    
    response=client.post('/post/Comment/',{'post_commented':post.id,'text':'test text for post'})
    
    assert response.status_code ==201
    
    assert response.data["text"] == 'test text for post'
    
    assert Comment.objects.count() == 1
    comment = Comment.objects.first()
    assert comment.profile_related == profile
  
#AUTH TEST  
@pytest.mark.django_db
def test_comment_create_not_login():
    client=APIClient()
    
    post=PostFactory()
   
    response=client.post('/post/Comment/',{'post_commented':post.id,'text':'test text for post'})
    
    assert response.status_code ==401
    
    assert Comment.objects.count() == 0

  

@pytest.mark.django_db
def test_comment_create_with_invalid_token():
    client=APIClient()
    
    post=PostFactory()
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer invalid token")
    
    response=client.post('/post/Comment/',{'post_commented':post.id,'text':'test text for post'})
    
    assert response.status_code ==401
    
    assert Comment.objects.count() == 0
   
  

#VALIDATION TEST
@pytest.mark.django_db
def test_comment_create_with_invalid_data():
    client=APIClient()
    
    post=PostFactory()
    profile=ProfileFactory()
    user=profile.user
    
    token=get_tokens_for_user(user)
 
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    #sending post obj instead of post id
    response=client.post('/post/Comment/',{'post_commented':post,'text':'test text for post'})
    
    assert response.status_code ==400
    
    assert Comment.objects.count() == 0
   