from django.contrib import admin
from accounts.models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class UserCustom(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']
