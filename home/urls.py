from django.conf.urls import patterns, url

urlpatterns = patterns('muhammetcan.home.views',
    url(r'^$', 'home'),
)
