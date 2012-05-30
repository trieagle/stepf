from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'stepf.views.home', name='home'),
    #url(r'^account/register','stepf.account.views.register'),
    url(r'^account/', include('stepf.account.urls')),
    url(r'^task/', include('stepf.task.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^$','stepf.account.views.index'),
)
