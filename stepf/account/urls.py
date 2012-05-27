from django.conf.urls import patterns, include, url

urlpatterns = patterns('stepf.account.views',
    url(r'$','index'),
    url(r'register/$','reg'),
    url(r'login/$','login'),
)
