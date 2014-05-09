from django.conf.urls import patterns, include, url

from .views import SignUpView,resource_list,verify

urlpatterns = patterns('',
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^list/$', resource_list, name='resource_list'),
    url(r'^verify/$',verify,name='verify')
)
