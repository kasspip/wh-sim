from django.conf.urls import url

import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'armory/', views.armory, name='armory'),
    url(r'army/(?P<pk>\d+)/$', views.armory_army_details, name='armory_army_details'),
    url(r'army/(?P<army_id>\d+)/figurine/$', views.armory_figurine_create, name='armory_figurine_create'),
    url(r'army/(?P<army_id>\d+)/figurine/(?P<pk>\d+)/$', views.armory_figurine_details, name='armory_figurine_details'),
    url(r'army/(?P<army_id>\d+)/figurine/(?P<pk>\d+)/edit/$', views.armory_figurine_edit, name='armory_figurine_edit'),
    url(r'army/(?P<army_id>\d+)/figurine/(?P<pk>\d+)/delete/$', views.armory_figurine_delete, name='armory_figurine_delete'),
]
