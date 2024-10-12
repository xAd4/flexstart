from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView
from .models import ServicesList, ServiceDetail

# Create your views here.

class ServiceDetail(DetailView):
    template_name = "services/service-details.html"
    model = ServiceDetail
    context_object_name = "services"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services_list"] = ServicesList.objects.all()
        return context