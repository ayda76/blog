from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from ..models import Post, StatusPost


@receiver(post_save, sender=Post)
def modify_post_status_posted(sender,instance,created,**kwargs):

    if created:
        Post.objects.filter(id=instance.id).update(status_post=StatusPost.POSTED)
#we do not use instance and save inorder to prevent loops    


