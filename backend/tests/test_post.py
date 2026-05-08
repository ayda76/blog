import pytest
from django.contrib.auth.models import User


def test_post_with_factory(db,post_factory):
    
    post_created=post_factory.create()

    print(post_created.title)
    print(post_created.profile_related.firstname)
    assert True 