"""
Definition of urls for DjangoGAE.
"""

from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('Guestbook.urls')),
    # Examples:
    # url(r'^$', 'DjangoGAE.views.home', name='home'),
    # url(r'^DjangoGAE/', include('DjangoGAE.DjangoGAE.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
