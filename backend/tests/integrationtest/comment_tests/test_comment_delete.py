import pytest
from rest_framework.test import APIClient
from tests.factories_profile import ProfileFactory
from tests.factories_post import PostFactory,CommentFactory
from blog_post_app.models import (Post,Comment)
from tests.integrationtest.post_tests.test_post_creation import get_tokens_for_user

# SUCCESS TESTS
@pytest.mark.django_db
def test_comment_delete_with_jwt():
    profile=ProfileFactory()
    user=profile.user
    token=get_tokens_for_user(user)
    
    client=APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    post=PostFactory()
    comment=CommentFactory(profile_related=profile,post_commented=post)
    response=client.delete(f'/post/Comment/{comment.id}/')

    assert response.status_code==204
    assert Comment.objects.count() ==0
    
@pytest.mark.django_db
def test_comment_delete_not_login():
    
    
    client=APIClient()
    profile=ProfileFactory()
    post=PostFactory()
    comment=CommentFactory(profile_related=profile,post_commented=post)
    response=client.delete(f'/post/Comment/{comment.id}/')

    assert response.status_code == 401
    assert Comment.objects.count() == 1
    
@pytest.mark.django_db
def test_comment_delete_with_invalid_token():
    profile=ProfileFactory()
   
    client=APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer invalid token')
    post=PostFactory()
    comment=CommentFactory(profile_related=profile,post_commented=post)
    response=client.delete(f'/post/Comment/{comment.id}/')

    assert response.status_code == 401
    
    assert Comment.objects.count() == 1
    
    
@pytest.mark.django_db
def test_comment_delete_with_wrong_profile():
    profile_comment=ProfileFactory()
    profile_strenger=ProfileFactory()
    user=profile_strenger.user
    token=get_tokens_for_user(user)
    
    client=APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    post=PostFactory()
    comment=CommentFactory(profile_related=profile_comment,post_commented=post)
    response=client.delete(f'/post/Comment/{comment.id}/')

    assert response.status_code == 401
    
    assert Comment.objects.count() == 1
    