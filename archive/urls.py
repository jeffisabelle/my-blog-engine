from django.conf.urls import patterns, url

urlpatterns = patterns('archive.views',
    url(r'^$', 'archive_generic'),
    url(r'c/(?P<category>.*?)$', 'archive_by_category'),
    url(r'y/(?P<year>.*?)$', 'archive_by_year'),
)
