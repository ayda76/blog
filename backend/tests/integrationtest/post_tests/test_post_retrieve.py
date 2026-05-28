import pytest
from rest_framework.test import APIClient
from tests.factories_post import PostFactory


@pytest.mark.django_db
def test_post_retrieve():
    
    client=APIClient()
    
    post=PostFactory(title="retrieve test")
    
    response=client.get(f'/post/Post/{post.id}/')
    
    assert response.status_code ==200
    
    assert response.data["title"] == "retrieve test"