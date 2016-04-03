from django.shortcuts import render, get_object_or_404
from .models import Person


def index(request):
    return render(request, 'cda/index.html')


def persons(request):
    all_persons = Person.objects.all().order_by('last_name', 'first_name')
    return render(request, 'cda/persons.html', {'all_persons': all_persons})


def person_profile(request, person_id):
    get_object_or_404(Person, pk=person_id)
    person = Person.objects.get(pk=person_id)
    return render(request, 'cda/person_profile.html', {'person': person})


def map_view(request):
    return render(request, 'cda/map_view.html')
