from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("status200/", views.Status202.as_view(), name="status200"),
]
