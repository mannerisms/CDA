from django.shortcuts import render, get_object_or_404
from .models import Person


def index(request):
    all_persons = Person.objects.all()
    return render(request, 'cda/index.html', {'all_persons': all_persons})
