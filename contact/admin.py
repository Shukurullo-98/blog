from django.contrib import admin
from .models import Contacts


# Register your models here.


@admin.register(Contacts)
class Contac(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'first_name', 'email']
