from rest_framework import serializers
from blog_profile_app.api.serializers import ProfileSerializer
from ..models import (Post,Comment)

class CommentSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model= Comment
        fields=['id','post_commented','profile_commented','text']       

class PostSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model= Post
        fields=['id','profile_related','title','description','status_post']
           

class PostGetSerializer(serializers.ModelSerializer):
    profile_related=ProfileSerializer(read_only=True)
    comment_post=CommentSimpleSerializer(required=False,read_only=True,many=True)
    class Meta:
        model= Post
        fields=['id','profile_related','title','description','status_post','comment_post']
        
class CommentGetSerializer(serializers.ModelSerializer):
    profile_commented=ProfileSerializer(read_only=True)
    post_commented=PostGetSerializer(read_only=True)
    class Meta:
        model= Comment
        fields=['id','post_commented','profile_commented','text']            
