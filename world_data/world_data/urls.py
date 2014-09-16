from django.conf.urls import patterns, urls, include

urlpatterns = patterns(
    '',
    (r'', include(urls, namespace='eggs', app_name='eggs')),
)
