# -*- coding: UTF-8-*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'guadiabike.views.home', name='home'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Login
    # url(r'^login/$', 'guadiabike.views.login', name='login'),

    url(r'^accounts/login/$', 'guadiabike.views.login', name='login'),
    url(r'^accounts/logout/$', 'guadiabike.views.logout', name='logout'),
    url(r'^home/$', 'guadiabike.views.home', name='home'),

    # Calendar - binky_calendar

    url(r'^calendar/', include('binky_calendar.urls', namespace='calendar')),

    # Administration - binky_admin

    url(r'^administration/', include('binky_admin.urls', namespace='administration')),

    # Usuarios - binky_user

    url(r'^user/', include('binky_user.urls', namespace='user')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
