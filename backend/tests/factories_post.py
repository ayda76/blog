import factory
from faker import Faker

from blog_post_app.models import (Post ,Comment)
from tests.factories_profile import ProfileFactory

fake=Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Post
    title = factory.Sequence(lambda n: f"title {n}")
    description = factory.Faker("text")
    profile_related=factory.SubFactory(ProfileFactory)
    
    
    
class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Comment
        
    text=factory.Faker("text")
    profile_commented=factory.SubFactory(ProfileFactory)
    post_commented=factory.SubFactory(PostFactory)
    