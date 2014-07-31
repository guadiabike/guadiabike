__author__ = 'Antonio'


from django.conf.urls import patterns, url
from binky_calendar import views


urlpatterns = patterns('',

    # Eventos
    url(r'^evento/detalle/(?P<evento_id>[0-9]+)/$', views.binky_calendar_evento_detalle, name='evento_detalle'),

    # AJAX - Eventos
    url(r'^evento/ajax/asiste/$', views.binky_calendar_evento_asiste, name='evento_asiste'),
)