# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from 選區資料.介面 import 看選區
from 選區資料.介面 import 看全部選區


urlpatterns = patterns('',
	url(r'^看選區/(?P<pk>\d+)$', 看選區, name = '看選區'),
	url(r'^.*$', 看全部選區, name = '看全部選區'),
)
