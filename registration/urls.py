from django.urls import path
from . import views as registration_views

urlpatterns = [
 path("signup/", registration_views.SignUpView.as_view(), name="signup"), # -> URL Sign Up
]