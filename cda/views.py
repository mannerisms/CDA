from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Person, CellMast


class PersonList(ListView):
    template_name = 'cda/persons.html'
    context_object_name = 'all_persons'

    def get_queryset(self):
        return Person.objects.all()


class PersonProfile(DetailView):
    model = Person
    template_name = 'cda/person_profile.html'


class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death',
              'person_gender', 'person_type', 'source', 'image', 'comment']


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death',
              'person_gender', 'person_type', 'source', 'image', 'comment']


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('cda:persons')


class MapView(ListView):
    template_name = 'cda/map_view.html'
    context_object_name = 'all_masts'

    def get_queryset(self):
        return CellMast.objects.all()


def index(request):
    return render(request, 'cda/index.html')
