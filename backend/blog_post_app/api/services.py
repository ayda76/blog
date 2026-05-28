from rest_framework.exceptions import ValidationError
from blog_profile_app.models import Profile


def add_profile(self,serializer):
        try:    
            profile_login=Profile.get_user_jwt(self,self.request)
            instance=serializer.save(profile_related=profile_login)
            return instance 
        except:
            raise ValidationError({"detail":"login problem"}) 
        
     