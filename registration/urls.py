from django.urls import path
from . import views as registration_views

urlpatterns = [
 path("signup/", registration_views.SignUpView.as_view(), name="signup"), 
 #path("profile/", registration_views.ProfileUpdateView.as_view(), name="profile"),
 path("profile/", registration_views.ProfileUpdateView.as_view(), name="profile-demo"),
 path("profile/email/", registration_views.EmailEditView.as_view(), name="profile-email"),
]