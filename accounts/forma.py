from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class Custom_UserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email']


class EditUserForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['first_name', 'last_name']
