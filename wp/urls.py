from django.conf.urls import patterns, url

urlpatterns = patterns('muhammetcan.wp.views',
    url(r'^$', 'show_posts'),
    url(r'categories/(?P<category>.*?)$', 'show_posts'),
    url(r'(?P<postname>.*?)$', 'single_post'),
)
