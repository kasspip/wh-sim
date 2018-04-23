# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class SimulatorIndex(TemplateView):
    template_name = 'simulator_index.html'
