# -*- coding: UTF-8-*-
__author__ = 'Antonio'


from django.conf.urls import patterns, url
from binky_admin import views


urlpatterns = patterns('',

    # Administración
    url(r'^$', views.binky_admin_index, name='admin_index'),

    url(r'^user/invitation/$', views.binky_admin_user_invitation, name='admin_user_invitation'),
    # AJAX - Eventos

)
