from django.conf.urls import url
from django.contrib import admin
from entries.views import EntryAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<entry_type>\w+)/', EntryAPIView.as_view(), name='entries'),
    # url(r'^$', HomeView.as_view(), name='home')
]
