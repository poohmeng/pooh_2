from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from views import *
from . import views
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),

    url(r'^contact/$', contact, name='contact'),
    url(r'^thanks/$', thanks, name='thanks'),
    url(r'^about/$', about, name='about'),

    # url(r'^blog/', include("blog.urls", namespace="blog")),

)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()