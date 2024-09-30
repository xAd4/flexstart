from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from contact.forms import ContactForm

# Create your views here.

class Home(TemplateView):
    template_name = "core/index.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)  # No guarda aún la instancia en la BD
            contact.user = request.user  # Asigna el usuario autenticado
            contact.save()  # Ahora guarda la instancia con el usuario
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Blog(TemplateView):
    template_name = "core/blog.html"

class BlogDetails(TemplateView):
    template_name = "core/blog-details.html"

class Service(TemplateView):
    template_name = "core/service-details.html"

class Portfolio(TemplateView):
    template_name = "core/portfolio-details.html"
