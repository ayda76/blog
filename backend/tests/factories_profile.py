import factory
from faker import Faker
from blog_profile_app.models import Profile
from tests.factories import UserFactory

fake=Faker()


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Profile
        
    user=factory.SubFactory(UserFactory)
    firstname=fake.name()
    lastname=fake.name()
    email='test@test.com'

 
