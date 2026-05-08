import pytest
from django.contrib.auth.models import User

#to run ::: pytest 
#to see the prints::pytest -rP
#to run just one testfile ::pytest tests/test_1.py
#to run just one  test function:: pytest tests/test_1.py::test1


##marks:
#@pytest.mark.skip :for skiping that test
#@pytest.mark.xfail : when you know a test will fail

#we can also assign markers in pytest.ini and only run the tests that have those marks like 


#fixtures will run once per test so we should assign scope for it like session or module inorder to run it once

#django will run the conftest file before any test
def test1():
    assert 1==1
    
    
    
    
@pytest.fixture
def fixture_1(scope='session'):
    return 2

def test_exp1(fixture_1):
    num= fixture_1
    assert num==2
    
    
    
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test','test@test.com','test')
    assert User.objects.count()==1
    
    
    
    
# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user('test-user')

#@pytest.mark.django_db
def test_set_check_password(user_1):
    assert user_1.username == 'test-user'
    # user_1.set_password('newpassword')
    # assert user_1.check_password('newpassword') is True
    
    
def test_new_user(new_user):
    print(new_user.first_name)
    assert new_user.first_name=='MyName'
    
### lowercase of UserFactory --> user_factory
def test_new_user_with_factory(user_factory):
    print(user_factory.username)
    assert True 
    
#if we want to make a user in test database we can use user_factory.build() but if we want to add it to the db we should get db with user_factory and use it like this: user_factory.create    
def test_new_user1_with_factory(db,user_factory):
    print(user_factory.username)
    user=user_factory.create()
    count=User.objects.all().count()
    print(count)
    print(user.username)
    assert True 