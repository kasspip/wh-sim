from django.conf.urls import url
from django.contrib import admin

from armory.views import ArmoryIndexView

app_name = 'armory'
urlpatterns = [
    url(r'', ArmoryIndexView.as_view(), name='index'),
]