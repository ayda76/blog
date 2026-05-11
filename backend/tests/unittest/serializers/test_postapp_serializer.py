from tests.factories_post import PostFactory
from blog_post_app.api.serializers import PostSerializer
import pytest

@pytest.mark.django_db
class TestPostSerializer:
    def test_serializer_output(self):    
        post=PostFactory()
        serializer_data=PostSerializer(post).data
        
        assert serializer_data['title'] is not None
        assert serializer_data['description'] is not None
        assert serializer_data['profile_related']['firstname'] == post.profile_related.firstname
        
    def test_partial_update(self):
        post=PostFactory()
        serializer=PostSerializer(post,data={'title':'testttt'},partial=True)
        assert serializer.is_valid()
        updated_post=serializer.save()
        assert updated_post.title == 'testttt'
        
    # def test_invalid_partial_update(self):
    #     post=PostFactory()
    #     serializer=PostSerializer(post,data={'profile_related':30},partial=True)
     
    #     assert  serializer.is_valid() == False
    #     print(f"serializer errors:::{serializer.errors}")
    #     assert 'email' in serializer.errors