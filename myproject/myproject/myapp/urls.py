# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list, build

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^build/(?P<user>\w+)/$', build, name='build')
]
