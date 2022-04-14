from django import forms
from mainapp.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'text', 'image', 'tags']
