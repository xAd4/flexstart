from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.Blog.as_view(), name="blog"),
    path("blog/details/<int:pk>/", views.BlogDetails.as_view(), name="blog-details"),
    # Delete Comment
    path("delete/<int:pk>/", views.CommentDeleteView.as_view(), name="comment-delete"),
]