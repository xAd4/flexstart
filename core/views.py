from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "core/index.html"

class Blog(TemplateView):
    template_name = "core/blog.html"

class BlogDetails(TemplateView):
    template_name = "core/blog-details.html"

class Service(TemplateView):
    template_name = "core/service-details.html"

class Portfolio(TemplateView):
    template_name = "core/portfolio-details.html"
