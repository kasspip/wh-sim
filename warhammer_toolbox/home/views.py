from django.shortcuts import render

from home.models import Figurine


def index(request):
    return render(request, 'index.html')


def armory(request):
    context = dict()
    context['figurines'] = Figurine.objects.all()
    return render(request, 'armory.html', context)


def armory_figurine_details(request, pk):
    context = dict()
    context['figurine'] = Figurine.objects.get(pk=pk)
    return render(request, 'armory_figurine_details.html', context)