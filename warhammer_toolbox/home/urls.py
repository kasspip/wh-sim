from django.conf.urls import url

from .views import index, armory, armory_figurine_details
from django.contrib import admin


urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'armory/', armory, name='armory'),
    url(r'figurine/(?P<pk>\d+)/$', armory_figurine_details, name='armory_figurine_details'),

]
