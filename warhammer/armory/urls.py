from django.conf.urls import url

from armory.views import ArmoryIndex

app_name = 'armory'
urlpatterns = [
    url(r'', ArmoryIndex.as_view(), name='index'),
]