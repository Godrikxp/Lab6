from django.conf.urls.defaults import *
#from mysite.views import hello

urlpatterns = patterns('',
	('^ajax/$', 'mysite.views.lab6ajax'),
	('^postajax/$', 'mysite.views.postajax'),
)

