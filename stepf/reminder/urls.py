from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'stepf.reminder.views',
    url(r'create_reminder/$', 'create_reminder'),
    url(r'remove_reminder/$', 'remove_reminder'),
    url(r'done_reminder/$', 'done_reminder'),
)

urlpatterns += patterns('',
    url(r'overview_reminder/$','stepf.views.overview_reminder'),
)
