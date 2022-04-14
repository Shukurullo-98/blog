from .models import Comment
from django import forms


class CommentUser(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
