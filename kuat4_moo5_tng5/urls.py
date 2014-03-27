from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'罷免/', include('罷免進度.網址')),
	url(r'^', include('選區資料.網址')),
)
