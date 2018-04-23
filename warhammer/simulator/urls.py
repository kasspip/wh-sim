from django.conf.urls import url

from simulator.views import SimulatorIndex

urlpatterns = [
    url(r'', SimulatorIndex.as_view(), name='simulator-index'),
]