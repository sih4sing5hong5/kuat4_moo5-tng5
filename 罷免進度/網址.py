from django.conf.urls import patterns, url
from 罷免進度.介面 import 看全部罷免
from 罷免進度.介面 import 罷免資訊


urlpatterns = patterns('',
	url(r'^罷免資訊/(?P<pk>\d+)$', 罷免資訊, name = '罷免資訊'),
	url(r'^.*$', 看全部罷免, name = '看全部罷免'),
)
