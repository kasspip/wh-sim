from django.conf.urls import url

from simulator.views import SimulatorIndexView

urlpatterns = [
    url(r'', SimulatorIndexView.as_view(), name='simulator-index'),
]