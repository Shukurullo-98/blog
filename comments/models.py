from django.utils import timezone
from django.db import models
from mainapp.models import Posts
from accounts.models import CustomUser


# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_author')
    text = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comment')
    # date = models.DateField(auto_now_add=True, default=timezone.now())
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)
