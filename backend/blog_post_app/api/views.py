
from rest_framework import generics, viewsets

from .services import add_profile

from ..permissions import (Post_Permissions,Comment_Permissions)
from ..models import (Post,Comment)
from .serializers import (PostSimpleSerializer,
                          CommentSimpleSerializer,
                          PostGetSerializer,
                          CommentGetSerializer)




class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes=[Post_Permissions]   
    pagination_class=None
    my_tags = ["Post"]
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT','PATCH']:
            return PostSimpleSerializer
        else:
            return PostGetSerializer
        
    def perform_create(self, serializer):
        instance=add_profile(self,serializer)
        return instance
    
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes=[Comment_Permissions]

    pagination_class=None
    my_tags = ["Post"]
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT','PATCH']:
            return CommentSimpleSerializer
        else:
            return CommentGetSerializer
        
    def perform_create(self, serializer):
        instance=add_profile(self,serializer)
        return instance
        
    