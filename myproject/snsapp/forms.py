from dataclasses import fields
from django import forms
from .models import Post, Comment

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields='__all__'


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comment']




    


