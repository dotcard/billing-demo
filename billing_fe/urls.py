from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^billing/', include('billing.urls')),
    url(r'^billing', include('billing.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin', include(admin.site.urls)),
    url(r'^', 'views.main'),
)
