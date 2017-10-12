from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('micropost.views',
    url(r'^$', 'index'),
    url(r'^create/$','create'),
    url(r'^(?P<micro_post_id>\d+)/$', 'detail'),
)