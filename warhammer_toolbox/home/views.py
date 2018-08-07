from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from home import forms
from home.models import Profile, Army, Role, Unit, Race


def update_instance(instance, data):
    for k, v in data.iteritems():
        setattr(instance, k, v)
    instance.save()


def index(request):
    return render(request, 'index.html')


def armory(request):

    context = dict()
    context['races'] = Race.objects.all()
    context['armies'] = Army.objects.all()
    return render(request, 'armory/armory.html', context)


# ----------------- Army CRUD ------------------------


def armory_army_create(request, race_id):
    race = get_object_or_404(Race, pk=race_id)

    if request.method == 'POST':
        form = forms.ArmyForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['race'] = race
            Army.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('home:armory'))
    else:
        form = forms.ArmyForm()

    context = dict()
    context['form'] = form
    context['race'] = race
    return render(request, 'armory/army/army_create.html', context)


def armory_army_details(request, army_id):
    context = dict()
    context['army'] = get_object_or_404(Army, pk=army_id)
    context['units'] = Unit.objects.filter(army=context['army'])
    context['roles'] = Role.objects.all()
    return render(request, 'armory/army/army_details.html', context)


def armory_army_edit(request, army_id):
    army = get_object_or_404(Army, pk=army_id)

    if request.method == 'POST':
        form = forms.ArmyForm(request.POST, request.FILES, instance=army)
        if form.is_valid():
            update_instance(army, form.cleaned_data)
            return HttpResponseRedirect(reverse('home:armory_army_details', kwargs={'army_id': army_id}))
    else:
        form = forms.ArmyForm(instance=army)

    context = dict()
    context['form'] = form
    context['army'] = army
    return render(request, 'armory/army/army_edit.html', context)


def armory_army_delete(request, army_id):
    army = get_object_or_404(Army, pk=army_id)
    army.delete()
    return HttpResponseRedirect(reverse('home:armory'))


# ----------------- Unit CRUD ------------------------


def armory_unit_create(request, army_id, role_id):
    army = get_object_or_404(Army, pk=army_id)
    role = get_object_or_404(Role, pk=role_id)

    if request.method == 'POST':
        form = forms.UnitForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['army'] = army
            form.cleaned_data['role'] = role
            Unit.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('home:armory_army_details', kwargs={'army_id': army_id}))
    else:
        form = forms.UnitForm()

    context = dict()
    context['form'] = form
    context['army'] = army
    return render(request, 'armory/unit/unit_create.html', context)


def armory_unit_details(request, army_id, unit_id):
    context = dict()
    context['army'] = get_object_or_404(Army, pk=army_id)
    context['unit'] = get_object_or_404(Unit, pk=unit_id)
    return render(request, 'armory/unit/unit_details.html', context)


def armory_unit_edit(request, army_id, unit_id):
    pass


def armory_unit_delete(request, army_id, unit_id):
    pass


# ----------------- Profile CRUD ------------------------


def armory_profile_create(request, army_id):
    army = get_object_or_404(Army, pk=army_id)

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.cleaned_data['army'] = army
            Profile.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('home:armory_army_details', kwargs={'army_id': army_id}))
    else:
        form = forms.ProfileForm()

    context = dict()
    context['form'] = form
    context['army'] = get_object_or_404(Army, pk=army_id)
    return render(request, 'armory/profile/profile_edit.html', context)


def armory_profile_details(request, army_id, pk):
    context = dict()
    context['figurine'] = get_object_or_404(Profile, pk=pk)
    context['army'] = get_object_or_404(Army, pk=army_id)
    return render(request, 'armory/profile/profile_details.html', context)


def armory_profile_edit(request, army_id, pk):
    figurine = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES, instance=figurine)
        if form.is_valid():
            update_instance(figurine, form.cleaned_data)
            return HttpResponseRedirect(reverse('home:armory_figurine_details', kwargs={'army_id': army_id, 'pk': pk}))
    else:
        form = forms.ProfileForm(instance=figurine)

    context = dict()
    context['form'] = form
    context['figurine'] = figurine
    context['army'] = get_object_or_404(Army, pk=army_id)
    context['armies'] = Army.objects.all()
    return render(request, 'armory/profile/profile_edit.html', context)


def armory_profile_delete(request, army_id, unit_id, profile_id):
    army = get_object_or_404(Army, pk=army_id)
    figurine = get_object_or_404(Profile, pk=pk)
    figurine.delete()
    return HttpResponseRedirect(reverse('home:armory_army_details', kwargs={'army_id': army.id}))


