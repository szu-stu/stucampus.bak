from django.conf.urls import patterns, include, url

from .views import SignUpView

urlpatterns = patterns('',
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
)
