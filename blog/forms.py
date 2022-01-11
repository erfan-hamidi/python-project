from django import forms
from django.forms import Form
from .models import Comment


class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        exclude = ["post"]
