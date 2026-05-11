from tests.factories_post import PostFactory
import pytest


@pytest.mark.django_db
class TestPostModel:
    def test_post_creation(self):
        post=PostFactory()
        assert post.id is not None
        
    def test_post_str(self):
        post=PostFactory()
        assert str(post) == post.title