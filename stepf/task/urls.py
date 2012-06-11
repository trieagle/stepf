from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'stepf.task.views',
    url(r'create_task/$', 'create_task'),
    url(r'remove_task/$', 'remove_task'),
    url(r'update_step/$', 'update_step'),
    url(r'update_nstep/$', 'update_nstep'),
    url(r'update_title/$', 'update_title'),
    url(r'update_message/$', 'update_message'),
)
urlpatterns += patterns('',
    url(r'overview_task/$','stepf.views.overview_task'),
)
