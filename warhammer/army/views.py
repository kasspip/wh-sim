# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class ArmyIndexView(TemplateView):
    template_name = 'army_index.html'
