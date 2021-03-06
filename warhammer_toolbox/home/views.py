from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from home import forms
from home.choices import DegressiveLargeNumericalEnum
from home.models import Profile, Army, Role, Unit, Race, DegressiveProfile


def update_instance(instance, data):
    for k, v in data.iteritems():
        setattr(instance, k, v)
    instance.save()

# ----------------- Register / Connect / disconnect ------------------------


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return render(request, 'index.html')
#     else:
#         return render(request, 'index.html')
#
#
# def logout_view(request):
#     logout(request)
#     return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def armory(request):
    context = dict()
    context['races'] = Race.objects.all()
    context['armies'] = Army.objects.all()
    return render(request, 'armory/armory.html', context)


# ----------------- Army CRUD ------------------------

@login_required
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


@login_required
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


@login_required
def armory_army_delete(request, army_id):
    army = get_object_or_404(Army, pk=army_id)
    army.delete()
    return HttpResponseRedirect(reverse('home:armory'))


# ----------------- Unit CRUD ------------------------


@login_required
def armory_unit_create(request, army_id, role_id):
    army = get_object_or_404(Army, pk=army_id)
    role = get_object_or_404(Role, pk=role_id)

    if request.method == 'POST':
        form = forms.UnitForm(request.POST, request.FILES)
        formset_profile = forms.ProfileCreateFormSet(request.POST, request.FILES)
        form_degressive_profile = forms.DegressiveProfileForm(request.POST, request.FILES)
        if form.is_valid() and formset_profile.is_valid() and form_degressive_profile.is_valid():
            # - unit save
            form.cleaned_data['army'] = army
            form.cleaned_data['role'] = role
            unit = Unit.objects.create(**form.cleaned_data)

            # - profile formsets save
            for profile_form in formset_profile.forms:
                delete = profile_form.cleaned_data.pop('DELETE')
                profile_form.cleaned_data['unit'] = unit
                profile = Profile.objects.create(**profile_form.cleaned_data)
                if profile.life == DegressiveLargeNumericalEnum.SPECIAL:
                    degressive_profile = DegressiveProfile.objects.create(**form_degressive_profile.cleaned_data)
                    profile.degressive = degressive_profile
                    profile.save()
            return HttpResponseRedirect(reverse('home:armory_army_details', kwargs={'army_id': army_id}))
    else:
        form = forms.UnitForm()
        formset_profile = forms.ProfileCreateFormSet()
        form_degressive_profile = forms.DegressiveProfileForm()

    context = dict()
    context['form'] = form
    context['army'] = army
    context['formset_profile'] = formset_profile
    context['form_degressive_profile'] = form_degressive_profile
    return render(request, 'armory/unit/unit_create.html', context)


def armory_unit_details(request, army_id, unit_id):
    context = dict()
    context['army'] = get_object_or_404(Army, pk=army_id)
    context['unit'] = get_object_or_404(Unit, pk=unit_id)
    context['profiles'] = context['unit'].profiles.all()
    return render(request, 'armory/unit/unit_details.html', context)


@login_required
def armory_unit_edit(request, army_id, unit_id):
    army = get_object_or_404(Army, pk=army_id)
    unit = get_object_or_404(Unit, pk=unit_id)
    if request.method == 'POST':
        form = forms.UnitForm(request.POST, request.FILES, instance=unit)
        formset_profile = forms.ProfileCreateFormSet(request.POST, request.FILES, instance=unit)
        degressive_form = forms.DegressiveProfileForm(request.POST, request.FILES, instance=unit.profile.degressive)

        if form.is_valid() and formset_profile.is_valid() and degressive_form.is_valid():
            # - unit save
            update_instance(unit, form.cleaned_data)

            # - profile formsets update or add
            for profile_form in formset_profile.forms:
                delete = profile_form.cleaned_data.pop('DELETE')
                profile_instance = profile_form.cleaned_data.pop('id')
                if profile_instance:
                    update_instance(profile_instance, profile_form.cleaned_data)
                else:
                    profile_instance = Profile.objects.create(**profile_form.cleaned_data)
                    profile_form.instance = profile_instance

            # - profile formsets delete
            unit.refresh_from_db()
            instances_updated = [form.instance.id for form in formset_profile.forms]
            for profile in unit.profiles.all():
                if profile.id not in instances_updated:
                    profile.delete()

            # - handle degressive profile
            unit.refresh_from_db()
            if unit.profile.life != DegressiveLargeNumericalEnum.SPECIAL:
                if unit.profile.degressive is not None:
                    unit.profile.degressive.delete()
                return HttpResponseRedirect(reverse('home:armory_unit_details', kwargs={
                    'army_id': army_id,
                    'unit_id': unit_id
                }))
            else:
                if unit.profile.degressive is not None:
                    update_instance(unit.profile.degressive, degressive_form.cleaned_data)
                else:
                    profile = unit.profile
                    degressive_profile = DegressiveProfile.objects.create(**degressive_form.cleaned_data)
                    profile.degressive = degressive_profile
                    profile.save()
            return HttpResponseRedirect(reverse('home:armory_unit_details', kwargs={
                    'army_id': army_id,
                    'unit_id': unit_id
                }))
    else:
        form = forms.UnitForm(instance=unit)
        formset_profile = forms.ProfileEditFormSet(instance=unit)
        degressive_form = forms.DegressiveProfileForm(instance=unit.profile.degressive)

    context = dict()
    context['unit'] = unit
    context['army'] = army
    context['form'] = form
    context['formset_profile'] = formset_profile

    context['form_degressive_profile'] = degressive_form
    return render(request, 'armory/unit/unit_edit.html', context)


@login_required
def armory_unit_delete(request, army_id, unit_id):
    army = get_object_or_404(Army, pk=army_id)
    unit = get_object_or_404(Unit, pk=unit_id)
    for profile in unit.profiles.all():
        if profile.degressive:
            profile.degressive.delete()
        profile.delete()
    unit.delete()
    return HttpResponseRedirect(reverse('home:armory_army_details', kwargs={'army_id': army.id}))
