from django.conf.urls import url, patterns

from stucampus.lecture.views import index, ManageView, auto_add


urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^manage/$', ManageView.as_view(), name='manage'),
    url(r'^auto_add/$', auto_add, name='auto_add'),
)
