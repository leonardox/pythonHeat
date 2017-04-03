# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list, build, list_stacks

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^build/(?P<user>\w+)/$', build, name='build'),
    url(r'^stacks/$', list_stacks, name='stacks'),
]
