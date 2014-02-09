from django.conf.urls import url, patterns

from stucampus.lecture.views import index, ManageView


urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^manage/$', ManageView.as_view(), name='manage'),
)
