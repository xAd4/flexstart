from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project

# Create your views here.

class Portfolio(DetailView):
    template_name = "portfolio/portfolio-details.html"
    model = Project
    context_object_name = "portfolio"

