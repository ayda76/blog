import factory
from faker import Faker
from blog_profile_app.models import Profile
from tests.factories import UserFactory


fake=Faker()


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Profile
        
    user=factory.SubFactory(UserFactory)
    firstname = factory.Faker("first_name")
    lastname = factory.Faker("last_name")
    email = factory.Sequence(lambda n: f"user{n}@test.com")

 
