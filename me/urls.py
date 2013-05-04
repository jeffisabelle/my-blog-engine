from django.conf.urls import patterns, url

urlpatterns = patterns('me.views',
    url(r'^$', 'me'),
    url(r'schedule.html', 'schedule'),
)
