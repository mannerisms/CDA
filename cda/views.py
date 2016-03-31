from django.shortcuts import render, get_object_or_404
from .models import Person


def index(request):
    return render(request, 'cda/index.html')


def persons(request):
    all_persons = Person.objects.all()
    return render(request, 'cda/persons.html', {'all_persons': all_persons})


def map_view(request):
    return render(request, 'cda/map_view.html')
