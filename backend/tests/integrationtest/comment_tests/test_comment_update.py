import pytest
from rest_framework.test import APIClient
from tests.factories_profile import ProfileFactory
from tests.factories_post import PostFactory,CommentFactory
from blog_post_app.models import (Post,Comment)
from tests.integrationtest.post_tests.test_post_creation import get_tokens_for_user

# SUCCESS TESTS
@pytest.mark.django_db
def test_comment_update_with_jwt():
    profile=ProfileFactory()
    user=profile.user
    token=get_tokens_for_user(user)
    
    client=APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    post=PostFactory()
    comment=CommentFactory(profile_related=profile,post_commented=post,text='old text')
    response=client.patch(f'/post/Comment/{comment.id}/',{'text':'new text'})

    assert response.status_code==200
    comment.refresh_from_db()
    assert Comment.objects.count() ==1
    assert response.data['text'] == 'new text'
   
#AUTH TEST  
@pytest.mark.django_db
def test_comment_update_not_login():
    profile=ProfileFactory()
    client=APIClient()
    post=PostFactory()
    
    comment=CommentFactory(profile_related=profile,post_commented=post,text='old text')
    response=client.patch(f'/post/Comment/{comment.id}/',{'text':'new text'})

    assert response.status_code==401
    comment.refresh_from_db()

    assert comment.text == 'old text'
  
@pytest.mark.django_db
def test_comment_update_with_invalid_token():
    client=APIClient()    
    profile=ProfileFactory()

    client.credentials(HTTP_AUTHORIZATION=f'Bearer invalid token')
    post=PostFactory()
    comment=CommentFactory(profile_related=profile,post_commented=post,text='old text')
    response=client.patch(f'/post/Comment/{comment.id}/',{'text':'new text'})

    assert response.status_code==401
    comment.refresh_from_db()

    assert comment.text == 'old text'
    
    
@pytest.mark.django_db
def test_comment_update_with_wrong_profile():
    profile_owner=ProfileFactory()
    profile_strenger=ProfileFactory()
    user=profile_strenger.user
    token=get_tokens_for_user(user)
    
    client=APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    post=PostFactory()
    comment=CommentFactory(profile_related=profile_owner,post_commented=post,text='old text')
    response=client.patch(f'/post/Comment/{comment.id}/',{'text':'new text'})
    
    assert response.status_code==401
    comment.refresh_from_db()

    assert comment.text == 'old text'


# VALIDATION TEST
@pytest.mark.django_db
def test_comment_update_with_invalid_data():
    profile=ProfileFactory()
    user=profile.user
    token=get_tokens_for_user(user)
    
    client=APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    post=PostFactory()
    comment=CommentFactory(profile_related=profile,post_commented=post,text='old text')
    response=client.patch(f'/post/Comment/{comment.id}/',{'text':''})

    
    assert response.status_code==400
    comment.refresh_from_db()

    assert comment.text == 'old text'