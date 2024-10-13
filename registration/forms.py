from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

class FormSignUpWithEmail(UserCreationForm): # -> Sign Up logic and security methods
    email = forms.EmailField(
        required=True,
        help_text="Required. 254 characters maximum and must be unique."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
    
## Profiles

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio", "url", "fullName", "company", "job", "country", "address", "phone", "twitter", "facebook", "instagram", "linkedin"]
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control-file mt-3"}),
            "bio": forms.Textarea(attrs={"class": "form-control mt-3", "rows": 3, "placeholder": "Biography"}),
            "url": forms.TextInput(attrs={"class": "form-control mt-3", "placeholder": "Personal URL"}),
            "fullName": forms.TextInput(attrs={"class": "form-control mt-3", "placeholder": "Personal URL"}),
            "company": forms.TextInput(attrs={"class": "form-control", "placeholder": "Company"}),
            "job": forms.TextInput(attrs={"class": "form-control", "placeholder": "Job"}),
            "country": forms.TextInput(attrs={"class": "form-control", "placeholder": "Country"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            "twitter": forms.URLInput(attrs={"class": "form-control", "placeholder": "Twitter Profile"}),
            "facebook": forms.URLInput(attrs={"class": "form-control", "placeholder": "Facebook Profile"}),
            "instagram": forms.URLInput(attrs={"class": "form-control", "placeholder": "Instagram Profile"}),
            "linkedin": forms.URLInput(attrs={"class": "form-control", "placeholder": "LinkedIn Profile"}),
        }


class ProfileEmailForm(UserChangeForm):
    email = forms.EmailField(required=True, help_text="Required. 254 characters maximum and must be unique.")

    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and email != self.instance.email: 
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists.")
        return email
