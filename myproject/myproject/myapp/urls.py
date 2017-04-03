# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list, build, list_stacks, create_stack, get_server

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^build/(?P<user>\w+)/$', build, name='build'),
    url(r'^stacks/$', list_stacks, name='stacks'),
    url(r'^create/(?P<name>\w+)/$', create_stack, name='create'),
    url(r'^detail/(?P<url>)/$', get_server, name='detail'),
]
