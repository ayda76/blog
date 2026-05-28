import pytest
from rest_framework.test import APIClient
from tests.factories_profile import ProfileFactory
from tests.factories_post import PostFactory,CommentFactory
from blog_post_app.models import Comment



@pytest.mark.django_db
def test_comment_retrieve():
    client=APIClient()
    profile=ProfileFactory()
    post=PostFactory()
    comment=CommentFactory(profile_related=profile,post_commented=post)
    
    response=client.get(f'/post/Comment/{comment.id}/')
    
    assert response.status_code == 200

    assert response.data['profile_related']['firstname']==profile.firstname