from django.conf.urls import patterns, include
from eggs import urls as eggs_urls

urlpatterns = patterns(
    '',
    (r'', include(eggs_urls, namespace='eggs', app_name='eggs')),
)
