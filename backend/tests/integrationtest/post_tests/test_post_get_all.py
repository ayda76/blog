import pytest
from rest_framework.test import APIClient
from tests.factories_profile import ProfileFactory
from tests.factories_post import PostFactory
from tests.integrationtest.post_tests.test_post_creation import get_tokens_for_user


@pytest.mark.django_db
def test_post_get_all():
    client=APIClient()
    
    profile=ProfileFactory()
    PostFactory.create_batch(3,profile_related=profile)
    
    response=client.get('/post/Post/')
    
    assert response.status_code ==200
    
    assert len(response.data) == 3