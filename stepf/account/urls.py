from django.conf.urls import patterns, include, url

# no chinese??

urlpatterns = patterns(
    'stepf.account.views',
    #url(r'$', 'index'), bug!
    url(r'login/$', 'login'),
    url(r'logout/$', 'logout'),
    url(r'register/$', 'register'),
    url(r'userinfo/$', 'userinfo'),

    url(r'','login'),# can't put this line on the top
)
