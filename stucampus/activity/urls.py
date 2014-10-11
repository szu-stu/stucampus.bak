from django.conf.urls import url, patterns
from stucampus.activity.views import index, ManageView


urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^manage/$', ManageView.as_view(), name='manage'),
)
