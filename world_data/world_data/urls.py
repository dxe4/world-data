from django.conf.urls import patterns, include
from spam import urls as spam_urls

urlpatterns = patterns(
    '',
    (r'', include(spam_urls, namespace='eggs', app_name='eggs')),
)
