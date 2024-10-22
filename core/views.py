from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from contact.forms import ContactForm
from services.models import ServiceDetail, ServicesList
from portfolio.models import Project
from testimonials.models import Testimonial
from registration.models import Profile

# Create your views here.
class Home(TemplateView):
    template_name = "core/index.html"
    success_url = reverse_lazy('status200')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        context["services"] = ServicesList.objects.all()
        context["services_detail"] = ServiceDetail.objects.all()
        context["projects"] = Project.objects.all()
        context["testimonials"] = Testimonial.objects.all()
        context["profiles"]  = Profile.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False) 
            contact.user = request.user  
            contact.save()  
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class Status202(TemplateView):
    template_name = "core/status-200.html"
