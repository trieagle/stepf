from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'stepf.account.views',
    #url(r'$', 'index'), bug!
    url(r'register/$', 'register'),
    url(r'login/$', 'login'),
    url(r'foo/$', 'foo'),
)
