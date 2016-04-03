from django.conf.urls import url
from . import views

app_name = 'cda'

urlpatterns = [
    # /cda/
    url(r'^$', views.index, name='index'),
    # /cda/sources/persons/

    url(r'^sources/persons/$', views.persons, name='persons'),
    # /cda/sources/persons/#

    # url(r'^sources/persons/profile/', views.person_profile, name='persons_profile'),
    url(r'^sources/persons/(?P<person_id>[0-9]+)/$', views.person_profile, name='persons_profile'),

    # /cda/map/
    url(r'^map/$', views.map_view, name='map_view'),
]