from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin
from django.db import models
from accounts.models import CustomUser
from taggit.managers import TaggableManager
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


# Create your models here.


class Posts(models.Model, HitCountMixin):
    NEW = (
        ("", ""),
        ("NEW", "NEW"),
    )

    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name= 'hit_count_generic_relation' )
    status = models.BooleanField(default=True, blank=True)
    new = models.CharField(choices=NEW, max_length=3, default='', blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='post/images')
    video = models.FileField(upload_to='post/video', null=True,blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def get_comment_count(self):
        return self.comment.count()
