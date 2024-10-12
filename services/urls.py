from django.urls import path
from . import views

urlpatterns = [
    path("service/<int:pk>/", views.ServiceDetail.as_view(), name="service-detail"),
]
