from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'muhammetcan.home.views.show_home'),
    url(r'^$', include('home.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^blog/', include('wp.urls')),
    url(r'^me/', include('me.urls')),
    url(r'^archive/', include('archive.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
