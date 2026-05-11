from django.db import models
from blog_profile_app.models import Profile
# Create your models here.

class Post(models.Model):
    title=models.TextField()
    description=models.TextField()
    image=models.FileField(upload_to='media/',blank=True,null=True)
    profile_related=models.ForeignKey(Profile,related_name='blog_profile',on_delete=models.CASCADE)
    liked_profiles=models.ManyToManyField(Profile,related_name='blog_profile_liked')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
