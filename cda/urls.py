from django.conf.urls import url
from . import views

app_name = 'cda'

urlpatterns = [
    # /cda/
    url(r'^$', views.index, name='index'),
]