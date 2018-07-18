# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from armory.models import Figurine


class FigurineIndexView(TemplateView):

    template_name = "armory_index.html"

    def get_context_data(self, **kwargs):
        context = super(FigurineIndexView, self).get_context_data(**kwargs)
        context['figurines'] = Figurine.objects.all()
        return context


class FigurineDetailView(TemplateView):

    template_name = "armory_figurine_details.html"

    def get_context_data(self, **kwargs):
        context = super(FigurineDetailView, self).get_context_data(**kwargs)
        return context