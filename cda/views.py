from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Person


class PersonList(generic.ListView):
    template_name = 'cda/persons.html'
    context_object_name = 'all_persons'

    def get_queryset(self):
        return Person.objects.all()


class PersonProfile(generic.DetailView):
    model = Person
    template_name = 'cda/person_profile.html'


class PersonProfileInline(generic.DetailView):
    model = Person
    template_name = 'cda/person_profile.html'


class PersonCreate(generic.CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'person_gender', 'person_type', 'Comment']


def index(request):
    return render(request, 'cda/index.html')


def person_profile(request, person_id):
    get_object_or_404(Person, pk=person_id)
    person = Person.objects.get(pk=person_id)
    return render(request, 'cda/person_profile.html', {'person': person})


def map_view(request):
    return render(request, 'cda/map_view.html')
