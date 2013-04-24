from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'muhammetcan.home.views.show_home'),
    url(r'^$', include('muhammetcan.home.urls')),
    url(r'^projects/', include('muhammetcan.projects.urls')),
    url(r'^blog/', include('muhammetcan.wp.urls')),
    url(r'^admin/', include(admin.site.urls)),


    # Examples:
    # url(r'^$', 'muhammetcan.views.home', name='home'),
    # url(r'^muhammetcan/', include('muhammetcan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
