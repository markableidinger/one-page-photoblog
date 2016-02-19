"""Views for entries app."""
from rest_framework import generics
from .models import PhotoBlogEntry
from .pagination import EntryPagination
from .serializers import EntrySerializer
from django.views.generic import ListView

class HomeView(ListView):
    model = PhotoBlogEntry
    queryset = PhotoBlogEntry.objects.orderby('-date')[:10]


class EntryAPIView(generics.ListAPIView):
    """GET requests return a JSON blob representing PhotoBlogEntry objects."""
    queryset = PhotoBlogEntry.objects.all()
    pagination_class = EntryPagination
    serializer_class = EntrySerializer
