"""Serializers for entries app."""

from rest_framework import serializers
from .models import PhotoBlogEntry


class EntrySerializer(serializers.ModelSerializer):
    """Serializes PhotoBlogEntry objects."""

    class Meta:
        model = PhotoBlogEntry
        fields = '__all__'
