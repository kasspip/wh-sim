# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class ArmoryIndex(TemplateView):
    template_name = 'armory_index.html'
