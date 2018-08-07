from django.conf.urls import url

import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),

    # armory
    url(r'armory/$', views.armory, name='armory'),
    url(r'armory/(?P<race_id>\d+)/create$', views.armory_army_create, name='armory_army_create'),
    url(r'armory/(?P<army_id>\d+)/$', views.armory_army_details, name='armory_army_details'),
    url(r'armory/(?P<army_id>\d+)/edit$', views.armory_army_edit, name='armory_army_edit'),
    url(r'armory/(?P<army_id>\d+)/delete$', views.armory_army_delete, name='armory_army_delete'),

    url(r'armory/(?P<army_id>\d+)/unit/(?P<role_id>\d+)/create$', views.armory_unit_create, name='armory_unit_create'),
    url(r'armory/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/$', views.armory_unit_details, name='armory_unit_details'),
    # url(r'armory/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/edit/$', views.armory_unit_edit, name='armory_unit_edit'),
    # url(r'armory/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/delete/$', views.armory_unit_delete, name='armory_unit_delete'),

    # url(r'army/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/profile$', views.armory_profile_create, name='armory_profile_create'),
    # url(r'army/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/profile/(?P<profile_id>\d+)/$', views.armory_profile_details, name='armory_profile_details'),
    # url(r'army/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/profile/(?P<profile_id>\d+)/edit/$', views.armory_profile_edit, name='armory_profile_edit'),
    # url(r'army/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/profile/(?P<profile_id>\d+)/delete/$', views.armory_profile_delete, name='armory_profile_delete'),
]
