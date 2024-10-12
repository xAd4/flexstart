from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("blog/", views.Blog.as_view(), name="blog"),
    path("blog/details/", views.BlogDetails.as_view(), name="blog-details"),
    path("status200/", views.Status202.as_view(), name="status200"),
]
