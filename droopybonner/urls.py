from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'droopybonner.views.home', name='home'),
    # url(r'^droopybonner/', include('droopybonner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'shipman.views.index'),
    url(r'^analyze/$', 'shipman.views.analyze_stats'),
    url(r'^track/$', 'shipman.views.track_package_form'),
    url(r'^track/(?P<tracking_number>.+)/$', 'shipman.views.track_package'),
)
