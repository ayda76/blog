import pytest
from rest_framework.test import APIClient
from tests.factories_profile import ProfileFactory
from tests.factories_post import PostFactory
from tests.integrationtest.post_tests.test_post_creation import get_tokens_for_user


@pytest.mark.django_db
def test_post_patch():
    client=APIClient()
    profile=ProfileFactory()
    post=PostFactory(profile_related=profile)
    
    token=get_tokens_for_user(profile.user)
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    
    response=client.patch(f'/post/Post/{post.id}/',{'title':'new test title'})
    
    assert response.status_code == 200
    post.refresh_from_db()
    assert response.data["title"] == 'new test title'
    assert post.profile_related == profile
    assert post.title == 'new test title'
    
    

@pytest.mark.django_db
def test_post_patch_not_logged_in():
    client=APIClient()
    post=PostFactory(title='original')
    
    response=client.patch(f'/post/Post/{post.id}/',{'title':'new test title'})
    post.refresh_from_db()
    assert response.status_code == 401
    assert post.title == 'original'
    
@pytest.mark.django_db
def test_post_patch_with_wrong_profile():
    client=APIClient()
    profile_owner=ProfileFactory()
    profile_strenger=ProfileFactory()
    post=PostFactory(profile_related=profile_owner,title='original')
    token=get_tokens_for_user(profile_strenger.user)
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    response=client.patch(f'/post/Post/{post.id}/',{'title':'new test title'})
    post.refresh_from_db()
    assert response.status_code == 401
    assert post.title == 'original'

@pytest.mark.django_db
def test_post_patch_post_not_exist():
    client=APIClient()
    profile=ProfileFactory()
   
    token=get_tokens_for_user(profile.user)
    
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    response=client.patch(f'/post/Post/99999/',{'title':'new test title'})
    
    assert response.status_code == 404 