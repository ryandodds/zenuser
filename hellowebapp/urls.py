from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'collection.views.index', name='home'),
    url(r'^about/$',
		TemplateView.as_view(template_name='about.html'),
		name='about'), 
    url(r'^contact/$',
		TemplateView.as_view(template_name='contact.html'),
		name='contact'),
    url(r'^interviews/(?P<slug>[-\w]+)/$', 
    	'collection.views.interview_detail', 
    	name='interview_detail'),
    url(r'^interviews/(?P<slug>[-\w]+)/edit/$', 
    	'collection.views.edit_interview', name='edit_interview'),
    url(r'^admin/', include(admin.site.urls)),
)
