from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import *

router = DefaultRouter()
router.register("profile", ProfileViewSet)

urlpatterns = [

    path("", include(router.urls)),
    path('change/password/', PasswordChangeView.as_view()),
    path('SignUp/', RegisterView.as_view(), name='signup'),
    path('Login/', LoginView.as_view(), name='login'),
    path('ME/', ProfileMeViewSet.as_view(), name='me'),

]
