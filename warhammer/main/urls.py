from django.conf.urls import url, include

from main.views import MainIndex

app_name = 'main'
urlpatterns = [
    url(r'^', MainIndex.as_view(), name='main-index'),
]