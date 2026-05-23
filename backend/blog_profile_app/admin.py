from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
# Register your models here.
from .models import Profile
from .resources import ProfileResource

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):

    list_display = ('id',)
    resource_class = ProfileResource