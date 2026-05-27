from rest_framework import permissions

from blog_profile_app.models import Profile


class Post_Permissions(permissions.BasePermission):
   
    def has_permission(self, request,view):
      
        if  request.method=='POST':
            return self.can_create_post(request)
        
        return True
        
    def can_create_post(self, request):
        profile_logedin= Profile.get_user_jwt(self,request)
        if profile_logedin is not None:
            return True
        else: 
            return False
        
    def has_object_permission(self, request, view, obj):

        #get is safe method
        if request.method in permissions.SAFE_METHODS:
            return True

        profile_login = Profile.get_user_jwt(self, request)

        return obj.profile_related.id == profile_login.id     

            

class Comment_Permissions(permissions.BasePermission):
    
    def has_permission(self, request,view):
      
        if  request.method=='POST':
            return self.can_create_comment(request)
        
        return True
        
    def can_create_comment(self, request):
        profile_logedin= Profile.get_user_jwt(self,request)
        if profile_logedin is not None:
            return True
        else: 
            
            return False
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        profile_login = Profile.get_user_jwt(self, request)

        return obj.profile_commented.id == profile_login.id     
