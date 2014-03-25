from django.conf.urls import patterns, url
from 選區資料.介面 import 看選區


urlpatterns = patterns('',
	url(r'^.*$', 看選區, name = '看選區'),
	url(r'^看選區$', 看選區, name = '看選區'),
)
