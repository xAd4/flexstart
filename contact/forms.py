from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","subject","message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu nombre"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Tu email"}  ),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Asunto"}),
            "message": forms.Textarea(attrs={"class": "form-control message-box mb-5", "placeholder": "Mensaje"}  ),
        }