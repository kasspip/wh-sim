from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView

from home.choices import Race
from home.forms import FigurineForm
from home.models import Figurine, Army


def index(request):
    return render(request, 'index.html')


def armory(request):
    context = dict()
    context['races'] = [Race.IMPERIUM, Race.CHAOS, Race.XENOS]
    context['armies'] = Army.objects.all()
    return render(request, 'armory.html', context)


def armory_army_details(request, pk):
    context = dict()
    context['army'] = Army.objects.get(pk=pk)
    context['figurines'] = Figurine.objects.filter(army=context['army'])
    return render(request, 'armory_army_details.html', context)


def armory_figurine_create(request):

    if request.method == 'POST':
        form = FigurineForm(request.POST)
        if form.is_valid():
            Figurine.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('home:armory'))
    else:
        form = FigurineForm()

    context = dict()
    context['form'] = form
    return render(request, 'armory_figurine_edit.html', context)


def armory_figurine_details(request, pk):
    figurine = get_object_or_404(Figurine, pk=pk)

    context = dict()
    context['figurine'] = figurine
    return render(request, 'armory_figurine_details.html', context)


def armory_figurine_edit(request, pk):
    figurine = get_object_or_404(Figurine, pk=pk)

    if request.method == 'POST':
        form = FigurineForm(request.POST)
        if form.is_valid():
            for k, v in form.cleaned_data.iteritems():
                setattr(figurine, k, v)
            figurine.save()
            return HttpResponseRedirect(reverse('home:armory_figurine_details', kwargs={'pk': pk}))
    else:
        form = FigurineForm(instance=figurine)

    context = dict()
    context['form'] = form
    context['figurine'] = figurine
    context['armies'] = Army.objects.all()
    return render(request, 'armory_figurine_edit.html', context)


def armory_figurine_delete(request, pk):
    figurine = get_object_or_404(Figurine, pk=pk)
    figurine.delete()
    return HttpResponseRedirect(reverse('home:armory'))


