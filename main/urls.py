from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^current', views.current, name='current'),
    url(r'^submit', views.submit, name='submissions'),
    url(r'^archive', views.archive, name='archive'),
]