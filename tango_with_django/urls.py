from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import rango.urls

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tango_with_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include(rango.urls)),
)
