from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormSignUpWithEmail  # Asegúrate de que el import del formulario es correcto

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