from django.conf.urls import patterns, url
from billing import views

urlpatterns = patterns('',
  url(r'^$', views.index, name = 'index'),
  url(r'^/(?P<customer_id>\d+)/$', views.detail, name = 'detail')
)