__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('web.urls', namespace='web')),
]