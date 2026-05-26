import pytest

from tests.factories_post import (PostFactory, CommentFactory)
from blog_post_app.api.serializers import (PostSimpleSerializer,
                                           CommentSimpleSerializer,
                                           PostGetSerializer,
                                           CommentGetSerializer)

@pytest.mark.django_db
class TestPostSerializer:
    def test_serializer_output(self):    
        post=PostFactory()
        serializer_data=PostGetSerializer(post).data
        
        assert serializer_data['title'] is not None
        assert serializer_data['description'] is not None
        assert serializer_data['profile_related']['firstname'] == post.profile_related.firstname
        
    def test_partial_update(self):
        post=PostFactory()
        serializer=PostSimpleSerializer(post,data={'title':'testttt'},partial=True)
        assert serializer.is_valid()
        updated_post=serializer.save()
        assert updated_post.title == 'testttt'
        
    def test_invalid_partial_update(self):
        post=PostFactory()
        serializer=PostSimpleSerializer(post,data={'profile_related':None},partial=True)
     
        assert  serializer.is_valid() == False
        print(f"serializer errors:::{serializer.errors}")

@pytest.mark.django_db
class TestCommentSerializer:
    def test_serializer_output(self):
        comment=CommentFactory()
        serializer_data=CommentGetSerializer(comment).data
        
        assert serializer_data['post_commented']['title']==comment.post_commented.title
        assert serializer_data['profile_commented']['email']==comment.profile_commented.email
        
    def test_partial_update(self):
        comment=CommentFactory()
        serializer=CommentSimpleSerializer(comment,data={'text':'test test'},partial=True)
        
        assert serializer.is_valid() ==True
        assert serializer.validated_data['text'] =='test test'
        updated_comment=serializer.save()
        assert updated_comment.text =='test test'
        
    def test_invalid_partial_update(self):
        comment=CommentFactory()
        serializer=CommentSimpleSerializer(comment,data={'post_commented':'test'},partial=True)
     
        assert  serializer.is_valid() == False
        print(f"serializer errors:::{serializer.errors}")
        serializer=CommentSimpleSerializer(comment,data={'profile_commented':700},partial=True)
     
        assert  serializer.is_valid() == False
        print(f"serializer errors:::{serializer.errors}")