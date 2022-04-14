from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=300, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='images/', blank=True, default="../static/User_Avatar_2.png")
    back_avatar = models.ImageField(upload_to='images', blank=True, default="../static/back1.jpg")
    telegram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    data_modified = models.DateTimeField(auto_now_add=True)
    data_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

    #
    # def get_user_profil(self):
    #     if self.avatar and hasattr(self.avatar, 'url'):
    #         return self.avatar.url
    #     else:
    #         return 'static/User_Avatar_2.png'
    #
    #
    # def get_user_back_avatar(self):
    #     if self.back_avatar and hasattr(self.back_avatar, 'url'):
    #         return self.back_avatar.url
    #     else:
    #         return 'static/back1.png'
