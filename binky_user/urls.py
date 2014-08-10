# -*- coding: UTF-8-*-

__author__ = 'Antonio'


from django.conf.urls import patterns, url
from binky_user import views


urlpatterns = patterns('',

    # Eventos
    url(r'^invitation/(?P<invitation_uuid>[0-9a-f-]{36})', views.binky_user_user_invitation, name='user_invitation'),

    # AJAX - Eventos
    #url(r'^ajax/example/$', views.binky_user_ajax_example, name='user_ajax_example'),
)