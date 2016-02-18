"""Admin for entries app."""
from django.contrib import admin
from .models import PhotoBlogEntry


class EntryAdmin(admin.ModelAdmin):
    """Admin for PhotoBlogEntry object. Currently just the default."""

    pass

admin.site.register(PhotoBlogEntry, EntryAdmin)
