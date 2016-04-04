from django.conf.urls import url
from . import views

app_name = 'cda'

urlpatterns = [
    # /cda/
    url(r'^$', views.index, name='index'),

    # /cda/sources/persons/
    url(r'^sources/persons/$', views.PersonList.as_view(), name='persons'),


    # /cda/sources/persons/#
    url(r'^sources/persons/(?P<pk>[0-9]+)/$', views.PersonProfile.as_view(), name='persons_profile'),

    # /cda/sources/persons/add/
    url(r'^sources/persons/add/$', views.PersonCreate.as_view(), name='person-add'),

    # /cda/map/
    url(r'^map/$', views.map_view, name='map_view'),
]
