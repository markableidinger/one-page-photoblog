"""Models used by Photoblog entries."""
from django.db import models
from django.contrib.postgres.fields import JSONField

class PhotoBlogEntry(models.Model):
    """The model for a blog entry."""

    title = models.CharField(max_length=200, verbose_name='Title')
    post_body = models.TextField(verbose_name='Post Body')
    metadata = JSONField(default=dict)
    photo_file = models.FileField()
    date = models.DateField()
    location_name = models.CharField(max_length=100)
