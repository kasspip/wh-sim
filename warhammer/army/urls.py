from django.conf.urls import url

from army.views import ArmyIndex

urlpatterns = [
    url(r'', ArmyIndex.as_view(), name='army-index'),
]