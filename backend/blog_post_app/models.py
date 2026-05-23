from django.db import models
from blog_profile_app.models import Profile
# Create your models here.

class StatusPost(models.TextChoices):
    
    PENDING = "draft", "draft"      
    ACCEPTED = "posted", "posted"     


class Post(models.Model):
    status_post=models.CharField(default='draft',max_length=10,choices=StatusPost.choices)
    title=models.TextField()
    description=models.TextField()
    image=models.FileField(upload_to='media/',blank=True,null=True)
    profile_related=models.ForeignKey(Profile,related_name='blog_profile',on_delete=models.CASCADE)
    liked_profiles=models.ManyToManyField(Profile,related_name='blog_profile_liked')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post_commented=models.ForeignKey(Post,related_name='comment_post',on_delete=models.CASCADE,null=True)
    profile_commented=models.ForeignKey(Profile,related_name='comment_profile',on_delete=models.CASCADE)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.profile_commented.firstname