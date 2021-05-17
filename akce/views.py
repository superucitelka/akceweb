from django.shortcuts import render
from django.views.generic import ListView

from .models import Akce


def index(request):
    context = {
        'nadpis': 'Web akcí',
    }

    return render(request, 'index.html', context=context)


class AkceListView(ListView):
    model = Akce
    template_name = 'list.html'
    context_object_name = 'seznam_akci'