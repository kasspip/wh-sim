# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView

from armory.forms import FigurineForm
from armory.models import Figurine


class ArmoryIndexView(ListView):
    # template_name = 'armory_index.html'
    # form_class = FigurineForm

    def get_queryset(self):
        return Figurine.objects.all()