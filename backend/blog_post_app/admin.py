from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
# Register your models here.
from .models import (Post,Comment)
from .resources import (PostResource,CommentResource)

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):

    list_display = ('id',)
    resource_class = PostResource

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):

    list_display = ('id',)
    resource_class = CommentResource