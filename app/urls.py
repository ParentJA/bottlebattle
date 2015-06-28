__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
    url(r'^$', 'home_view', name='home'),
    url(r'^event/$', 'event_view', name='event'),
    url(r'^event/new/$', 'new_event_view', name='new_event'),
)