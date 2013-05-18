from django.conf.urls import patterns, url

urlpatterns = patterns('archive.views',
    url(r'^$', 'archive_generic'),
)
