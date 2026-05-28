import pytest
from rest_framework.test import APIClient
from tests.factories_post import CommentFactory
from blog_post_app.models import Comment



@pytest.mark.django_db
def test_comment_get_all():
    client=APIClient()
    CommentFactory.create_batch(3)
    
    response=client.get('/post/Comment/')
    
    assert response.status_code == 200
    assert Comment.objects.count() == 3