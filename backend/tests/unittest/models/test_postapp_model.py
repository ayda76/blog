import pytest
from tests.factories_post import (PostFactory,CommentFactory)
from tests.factories_profile import ProfileFactory



@pytest.mark.django_db
class TestPostModel:
    def test_post_creation(self):
        post=PostFactory()
        assert post.id is not None
        
    def test_post_str(self):
        post=PostFactory()
        assert str(post) == post.title
        
        
@pytest.mark.django_db
class TestCommentModel:
    def test_comment_creation(self):
        comment=CommentFactory()
        assert comment.id is not None
        
    def test_comment_str(self):
        comment=CommentFactory()
        assert str(comment)==comment.profile_related.firstname
        
    def test_post_profile_relations(self):
        post=PostFactory()
        profile=ProfileFactory()
        comment=CommentFactory(post_commented=post,profile_related=profile)
        
        assert comment.post_commented.title==post.title
        assert comment.profile_related.firstname==profile.firstname