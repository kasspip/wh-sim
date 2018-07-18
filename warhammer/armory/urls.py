from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from armory.views import FigurineDetailView, FigurineIndexView

app_name = 'armory'
urlpatterns = [
    url(r'', FigurineIndexView.as_view(), name='index'),
    url(r'figurine/(?P<pk>\d+)/', FigurineDetailView.as_view(), name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)