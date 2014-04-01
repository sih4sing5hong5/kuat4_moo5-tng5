# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from 罷免進度.介面 import 看全部罷免
from 罷免進度.介面 import 罷免資訊
from 罷免進度.介面 import 改罷免


urlpatterns = patterns('',
	url(r'^罷免資訊/(?P<pk>\d+)$', 罷免資訊, name = '罷免資訊'),
	url(r'^新罷免$', 改罷免, name = '新罷免'),
	url(r'^改罷免/(?P<pk>\d+)$', 改罷免, name = '改罷免'),
	url(r'^.*$', 看全部罷免, name = '看全部罷免'),
)
