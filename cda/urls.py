from django.conf.urls import url
from . import views

app_name = 'cda'

urlpatterns = [
    # /cda/
    url(r'^$', views.index, name='index'),
    url(r'^persons/$', views.persons, name='persons'),
    url(r'^map/$', views.map_view, name='map_view'),
]