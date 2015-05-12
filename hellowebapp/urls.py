from collection.backends import MyRegistrationView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'collection.views.index', name='interviews'),
    url(r'^objectives/$', TemplateView.as_view(template_name='objectives.html'), name='objectives'), 
    url(r'^debriefs/$', TemplateView.as_view(template_name='debriefs.html'), name='debriefs'),
    
    url(r'^interviews/(?P<slug>[-\w]+)/$', 'collection.views.interview_detail', name='interview_detail'),
    url(r'^interviews/(?P<slug>[-\w]+)/edit/$', 'collection.views.edit_interview', name='edit_interview'),

    url(r'^accounts/password/reset/$', password_reset, 
        {'template_name': 'registration/password_reset_form.html'}, 
        name="password_reset"),
    url(r'^accounts/password/reset/done/$', 
        password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, 
        {'template_name': 'registration/password_reset_confirm.html'}, 
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),

    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_interview/$', 'collection.views.create_interview', name='registration_create_interview'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
