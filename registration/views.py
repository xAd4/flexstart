from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import FormSignUpWithEmail, ProfileEmailForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import Profile

# System Sign Up

class SignUpView(CreateView):
    form_class = FormSignUpWithEmail
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy("login")

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form(form_class)
        form.fields["username"].widget = forms.TextInput(attrs={
            "class": "form-control mb-2",
            "placeholder": "Username"
        })
        form.fields["email"].widget = forms.EmailInput(attrs={
            "class": "form-control mb-2",
            "placeholder": "Email"
        })
        form.fields["password1"].widget = forms.PasswordInput(attrs={
            "class": "form-control mb-2",
            "placeholder": "Password"
        })
        form.fields["password2"].widget = forms.PasswordInput(attrs={
            "class": "form-control mb-2",
            "placeholder": "Repeat password"
        })
        return form
    
@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "registration/users_profile.html"
    success_url = reverse_lazy("profile-demo")

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        response = super().form_valid(form)
        full_name = self.request.POST.get('fullName')
        if full_name:
            first_name, *last_name = full_name.strip().split(' ', 1)
            self.request.user.first_name = first_name
            self.request.user.last_name = last_name[0] if last_name else ''
            self.request.user.save()
        email = self.request.POST.get('email')
        if email and email != self.request.user.email:
            self.request.user.email = email
            self.request.user.save()
        return response
    
@method_decorator(login_required, name="dispatch")
class EmailEditView(UpdateView):
    form_class = ProfileEmailForm
    template_name = "registration/profile_edit_email.html"
    success_url = reverse_lazy("profile-demo")

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailEditView, self).get_form(form_class)
        form.fields["email"].widget = forms.EmailInput(attrs={"class": "form-control mb-2", "placeholder": "Email"})
        return form

    def form_valid(self, form):
        messages.success(self.request, "Email updated successfully!")  # Mensaje de éxito
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the error below.")  # Mensaje de error
        return super().form_invalid(form)  # Asegúrate de que esto retorna el renderizado con errores