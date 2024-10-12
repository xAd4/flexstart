from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import CreateView
from .models import Testimonial

# Create your views here.

@method_decorator(staff_member_required, name="dispatch")
class TestimonialCreateView(CreateView):
    model = Testimonial
    template_name = "testimonials/form_create.html"
    fields = ["name", "testimonial", "profession", "image"]
    success_url = reverse_lazy("home")

    def get_form(self, form_class = None): 
        form = super(TestimonialCreateView, self).get_form()
        form.fields["name"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Name"})
        form.fields["testimonial"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Profession"})
        form.fields["profession"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder':"Testimonial"})
        form.fields["image"].widget = forms.ClearableFileInput()
        return form