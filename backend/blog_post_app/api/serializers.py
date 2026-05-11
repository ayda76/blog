from rest_framework import serializers
from blog_profile_app.api.serializers import ProfileSerializer
from blog_post_app.models import Post



class PostSerializer(serializers.ModelSerializer):
    profile_related=ProfileSerializer(read_only=True)
    class Meta:
        model= Post
        fields=['id','profile_related','title','description']