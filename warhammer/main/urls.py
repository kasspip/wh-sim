from django.conf.urls import url, include

from main.views import MainIndex

app_name = 'main'
urlpatterns = [
    url(r'^', MainIndex.as_view(), name='main-index'),
    # url(r'^army/', include('army.urls', namespace='army'), name='army-index'),
    # url(r'^simulator/', include('simulator.urls', namespace='simulator'), name='simulator-index'),
]