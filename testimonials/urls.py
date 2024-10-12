from django.urls import path
from . import views

urlpatterns = [
    path("create/testimonial", views.TestimonialCreateView.as_view(), name="create-testimonial")
]
