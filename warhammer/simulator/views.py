# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class SimulatorIndexView(TemplateView):
    template_name = 'simulator_index.html'