from django.db import models


# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=80)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title
