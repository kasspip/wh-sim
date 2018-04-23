# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class MainIndex(TemplateView):
    template_name = 'main_index.html'

