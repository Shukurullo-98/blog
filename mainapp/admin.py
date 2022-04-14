from django.contrib import admin
from .models import Posts


# Register your models here.


@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    list_display = ['id', 'author', 'text', 'title']
