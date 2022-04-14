from django.contrib import admin
from comments.models import Comment


# Register your models here.


@admin.register(Comment)
class CommentUser(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'text']
