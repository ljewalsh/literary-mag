from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^journal/([0-9])/([0-9])', views.journal, name='journal'),
    url(r'^submit', views.submit, name='submissions'),
    url(r'^archive', views.archive, name='archive'),
    url(r'^froala_editor/', include('froala_editor.urls'))
]

