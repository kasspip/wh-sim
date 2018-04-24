from django.conf.urls import url

from army.views import ArmyIndexView

urlpatterns = [
    url(r'', ArmyIndexView.as_view(), name='army-index'),
]