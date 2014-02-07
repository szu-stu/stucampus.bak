from django.conf.urls import url, patterns
from stucampus.articles.views import PostView


urlpatterns = patterns(
    '',
    url(r'^manage/$', , name=''),
    url(r'^add/$', PostView.as_view(), name='add'),
    url(r'^modify/$', ModifyView.as_view(), name='modify'),
    url(r'^category/$', , name='modify'),
)
