from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'parent'] 

        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Comment*',
                'rows': 4 
            }),
        }

        labels = {
            'comment': '',  
        }
