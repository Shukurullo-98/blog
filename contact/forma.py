from django import forms

from contact.models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['first_name', 'text', 'title', 'email']
