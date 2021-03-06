from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy

import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {"template_name": "login.html"}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': reverse_lazy('home:login')}, name='logout'),

    # armory
    url(r'army/$', views.armory, name='armory'),
    url(r'army/(?P<race_id>\d+)/create$', views.armory_army_create, name='armory_army_create'),
    url(r'army/(?P<army_id>\d+)/$', views.armory_army_details, name='armory_army_details'),
    url(r'army/(?P<army_id>\d+)/edit$', views.armory_army_edit, name='armory_army_edit'),
    url(r'army/(?P<army_id>\d+)/delete$', views.armory_army_delete, name='armory_army_delete'),
    url(r'army/(?P<army_id>\d+)/unit/(?P<role_id>\d+)/create$', views.armory_unit_create, name='armory_unit_create'),
    url(r'army/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/$', views.armory_unit_details, name='armory_unit_details'),
    url(r'army/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/edit/$', views.armory_unit_edit, name='armory_unit_edit'),
    url(r'army/(?P<army_id>\d+)/unit/(?P<unit_id>\d+)/delete/$', views.armory_unit_delete, name='armory_unit_delete'),
]
