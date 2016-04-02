"""Serializers for entries app."""

from rest_framework import serializers
from .models import PhotoBlogEntry


class PhotoBlogEntrySerializer(serializers.ModelSerializer):
    """Serializes PhotoBlogEntry objects."""

    class Meta:
        model = PhotoBlogEntry
        fields = '__all__'


SERIALIZERS = {
    'photoblogentry': PhotoBlogEntrySerializer
}


def get_serializer_by_name(name):
    return SERIALIZERS[name]
