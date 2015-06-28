__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.conf.urls import patterns, url

urlpatterns = patterns('web.views',
    url(r'^$', 'home_view', name='home'),
)