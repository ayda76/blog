import pytest
from unittest.mock import MagicMock, patch
from blog_post_app.permissions import (Post_Permissions,Comment_Permissions)


@patch("blog_post_app.permissions.Profile.get_user_jwt")
def test_post_permission_post_logged_in(mock_get_user_jwt):
    # fake logged-in profile
    mock_profile = MagicMock()

    # هر وقت get_user_jwt صدا زده شد
    # این profile را برگردان
    mock_get_user_jwt.return_value = mock_profile
    # ساخت permission
    permission = Post_Permissions()
    # fake request
    request = MagicMock()
    request.method = "POST"
    # اجرای permission
    result = permission.has_permission(request,None)

    # بررسی نتیجه
    assert result is True
    
@patch("blog_post_app.permissions.Profile.get_user_jwt")
def test_post_permission_not_logged_in(mock_get_user_jwt):
    mock_get_user_jwt.return_value=None
    permission=Post_Permissions()
    request=MagicMock()
    request.method="POST"
    
    result=permission.has_permission(request,None)
    
    assert result ==False
    
    
def test_post_permisson_get_request():
    permission=Post_Permissions()
    
    request=MagicMock()
    request.method="GET"
    
    result=permission.has_permission(request,None)
    assert result == True
    
def test_post_permission_safe_method():
    permission=Post_Permissions()
    
    request=MagicMock()
    request.method="GET"
    obj = MagicMock()
    
    result=permission.has_object_permission(request,None,obj)
    
    assert result == True

@patch('blog_post_app.permissions.Profile.get_user_jwt')
def test_post_permission_with_profile(mock_get_user_jwt):
    profile=MagicMock()
    profile.id=1
    mock_get_user_jwt.return_value=profile
    permission=Post_Permissions()
    request=MagicMock()
    request.method="PUT"
    
    obj=MagicMock()
    obj.profile_related.id=1
    result=permission.has_object_permission(request,None,obj)
    
    assert result==True
    
@patch('blog_post_app.permissions.Profile.get_user_jwt')
def test_post_permission_without_profile(mock_get_user_jwt):
    profile=MagicMock()
    profile.id=1
    mock_get_user_jwt.return_value=profile
    permission=Post_Permissions()
    request=MagicMock()
    request.method="PATCH"
    
    obj=MagicMock()
    obj.profile_related.id=2
    result=permission.has_object_permission(request,None,obj)
    
    assert result==False
    
    
@patch("blog_post_app.permissions.Profile.get_user_jwt")
def test_comment_permission_profile_logged_in(mock_get_user_jwt):
   
    profile = MagicMock()
    mock_get_user_jwt.return_value = profile

    permission = Comment_Permissions()

    request = MagicMock()
    request.method = "POST"

    result = permission.has_permission(request,None)

    assert result == True
    
@patch("blog_post_app.permissions.Profile.get_user_jwt")
def test_comment_permission_not_logged_in(mock_get_user_jwt):
   
  
    mock_get_user_jwt.return_value =None

    permission = Comment_Permissions()

    request = MagicMock()
    request.method = "POST"

    result = permission.has_permission(request,None)

    assert result ==False
    
def test_comment_permission_get_request():

    permission = Comment_Permissions()

    request = MagicMock()
    request.method = "GET"

    result = permission.has_permission(request,None)

    assert result ==True   
    
def test_comment_permission_safe_method():

    permission = Comment_Permissions()

    request = MagicMock()
    request.method = "GET"
    obj=MagicMock()
    result = permission.has_object_permission(request,None,obj)

    assert result ==True   
    
    
@patch('blog_post_app.permissions.Profile.get_user_jwt')
def test_comment_permission_with_profile(mock_get_user_jwt):
    profile=MagicMock()
    profile.id=1
    mock_get_user_jwt.return_value=profile
    permission=Comment_Permissions()
    request=MagicMock()
    request.method="PATCH"
    
    obj=MagicMock()
    obj.profile_related.id=1
    result=permission.has_object_permission(request,None,obj)
    
    assert result==True
    
@patch('blog_post_app.permissions.Profile.get_user_jwt')
def test_comment_permission_without_profile(mock_get_user_jwt):
    profile=MagicMock()
    profile.id=1
    mock_get_user_jwt.return_value=profile
    permission=Comment_Permissions()
    request=MagicMock()
    request.method="PATCH"
    
    obj=MagicMock()
    obj.profile_related.id=2
    result=permission.has_object_permission(request,None,obj)
    
    assert result==False