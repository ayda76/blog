import pytest
from blog_post_app.models import StatusPost
from factories_post import PostFactory

@pytest.mark.django_db
def test_post_status_change_after_creation():
    
    post=PostFactory()
    
    post.refresh_from_db()
    assert post.status_post == StatusPost.POSTED