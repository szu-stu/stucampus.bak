from django.conf.urls import url, patterns

from .views import ApplyView, manage_list, app_view


urlpatterns = patterns(
    '',
    url(r'^$', ApplyView.as_view(), name='index'),
    url(r'^list/$', manage_list, name='list'),
    url(r'^view/$', app_view, name='view'),
)
