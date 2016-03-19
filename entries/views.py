"""Views for entries app."""
from rest_framework import generics
from .models import PhotoBlogEntry
from .pagination import EntryPagination
from .serializers import EntrySerializer
from django.views.generic import ListView


class HomeView(ListView):
    """The home view that users land on at url '/'."""

    model = PhotoBlogEntry
    queryset = PhotoBlogEntry.objects.order_by('-date')[:10]
    template_name = 'home.html'


class EntryAPIView(generics.ListAPIView):
    """GET requests return a JSON blob representing PhotoBlogEntry objects."""

    queryset = PhotoBlogEntry.objects.all()
    pagination_class = EntryPagination
    serializer_class = EntrySerializer
