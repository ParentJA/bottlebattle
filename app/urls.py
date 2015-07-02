__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
    url(r'^$', 'home_view', name='home'),
    url(r'^event/$', 'event_view', name='event'),
    url(r'^event/new/$', 'new_event_view', name='new_event'),
    url(r'^event/(?P<event_id>\d+)/$', 'event_detail_view', name='event_detail'),
    url(r'^event/list/$', 'event_list_view', name='event_list'),
)