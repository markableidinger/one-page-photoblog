"""Views for entries app."""
from rest_framework import generics
from .models import PhotoBlogEntry
from .pagination import EntryPagination
from .serializers import get_serializer_by_name
from django.views.generic import ListView
from django.apps import apps

# class HomeView(ListView):
#     """The home view that users land on at url '/'."""

#     model = PhotoBlogEntry
#     queryset = PhotoBlogEntry.objects.order_by('-date')[:10]
#     template_name = 'home.html'


class EntryAPIView(generics.ListAPIView):
    """GET requests return a JSON blob representing PhotoBlogEntry objects."""

    pagination_class = EntryPagination


    def get_serializer_class(self, *args, **kwargs):
        return get_serializer_by_name(self.kwargs['entry_type'])



    def get_queryset(self, *args, **kwargs):
        return apps.get_model('entries', self.kwargs['entry_type']).objects.all()
