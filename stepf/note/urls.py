from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'stepf.note.views',
    url(r'create_note/$', 'create_note'),
    url(r'remove_note/$', 'remove_note'),
    url(r'done_note/$', 'done_note'),
)
