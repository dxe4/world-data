from django.conf.urls import patterns, url
from eggs.views import index

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
)
