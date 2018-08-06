from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView

from home.choices import Race
from home.forms import FigurineForm
from home.models import Figurine, Army, Role


def index(request):
    return render(request, 'index.html')


def armory(request):
    context = dict()
    context['races'] = [Race.IMPERIUM, Race.CHAOS, Race.XENOS]
    context['armies'] = Army.objects.all()
    return render(request, 'armory.html', context)


def armory_army_details(request, pk):
    context = dict()
    context['army'] = get_object_or_404(Army, pk=pk)
    context['figurines'] = Figurine.objects.filter(army=context['army'])
    context['roles'] = Role.objects.all()
    return render(request, 'armory_army_details.html', context)


def armory_figurine_create(request, army_id):
    army = get_object_or_404(Army, pk=army_id)

    if request.method == 'POST':
        form = FigurineForm(request.POST)
        if form.is_valid():
            form.cleaned_data['army'] = army
            Figurine.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('home:armory_army_details', kwargs={'pk': army_id}))
    else:
        form = FigurineForm()

    context = dict()
    context['form'] = form
    context['army'] = get_object_or_404(Army, pk=army_id)
    return render(request, 'armory_figurine_edit.html', context)


def armory_figurine_details(request, army_id, pk):
    context = dict()
    context['figurine'] = get_object_or_404(Figurine, pk=pk)
    context['army'] = get_object_or_404(Army, pk=army_id)
    return render(request, 'armory_figurine_details.html', context)


def armory_figurine_edit(request, army_id, pk):
    figurine = get_object_or_404(Figurine, pk=pk)

    if request.method == 'POST':
        form = FigurineForm(request.POST, request.FILES, instance=figurine)
        if form.is_valid():
            for k, v in form.cleaned_data.iteritems():
                setattr(figurine, k, v)
            figurine.save()
            return HttpResponseRedirect(reverse('home:armory_figurine_details', kwargs={'army_id': army_id, 'pk': pk}))
    else:
        form = FigurineForm(instance=figurine)

    context = dict()
    context['form'] = form
    context['figurine'] = figurine
    context['army'] = get_object_or_404(Army, pk=army_id)
    context['armies'] = Army.objects.all()
    return render(request, 'armory_figurine_edit.html', context)


def armory_figurine_delete(request, army_id, pk):
    army = get_object_or_404(Army, pk=army_id)
    figurine = get_object_or_404(Figurine, pk=pk)
    figurine.delete()
    return HttpResponseRedirect(reverse('home:armory_army_details', kwargs={'pk': army.id}))


