from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'palavlarus.views.home', name='home'),
    # url(r'^palavlarus/', include('palavlarus.foo.urls')),
    url(r'^palavlarus/$', 'masterpiece.views.home', name='home'),
    url(r'^palavlarus/login/$', 'masterpiece.views.log_it', name='giris'),
    url(r'^palavlarus/(?P<the_word>.*)/$', 'masterpiece.views.word', name='word'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
