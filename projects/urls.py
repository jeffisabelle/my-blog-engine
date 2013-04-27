from django.conf.urls import patterns, url

urlpatterns = patterns('muhammetcan.projects.views',
    url(r'^$', 'projects'),
)
