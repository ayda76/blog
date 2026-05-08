import factory
from faker import Faker
from blog_post_app.models import Post
from tests.factories_profile import ProfileFactory

fake=Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Post
        
    
    title='test title'
    description=fake.text()
    profile_related=factory.SubFactory(ProfileFactory)