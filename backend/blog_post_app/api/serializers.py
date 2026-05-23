from rest_framework import serializers
from blog_profile_app.api.serializers import ProfileSerializer
from ..models import (Post,Comment)

class CommentSerializer(serializers.ModelSerializer):
    profile_commented=ProfileSerializer(read_only=True)
    class Meta:
        model= Comment
        fields=['id','post_commented','profile_commented','text']       
        

class PostSerializer(serializers.ModelSerializer):
    profile_related=ProfileSerializer(read_only=True)
    comment_post=CommentSerializer(required=False,read_only=True,many=True)
    class Meta:
        model= Post
        fields=['id','profile_related','title','description','status_post','comment_post']
        
        
