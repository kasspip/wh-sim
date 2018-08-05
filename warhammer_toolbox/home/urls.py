from django.conf.urls import url

from .views import index, armory, armory_figurine_details, armory_figurine_edit, armory_figurine_create, \
    armory_figurine_delete
from django.contrib import admin


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'test/', armory, name='test'),
    url(r'^admin/', admin.site.urls),
    url(r'armory/', armory, name='armory'),
    url(r'figurine/$', armory_figurine_create, name='armory_figurine_create'),
    url(r'figurine/(?P<pk>\d+)/$', armory_figurine_details, name='armory_figurine_details'),
    url(r'figurine/(?P<pk>\d+)/edit/$', armory_figurine_edit, name='armory_figurine_edit'),
    url(r'figurine/(?P<pk>\d+)/delete/$', armory_figurine_delete, name='armory_figurine_delete'),
]
