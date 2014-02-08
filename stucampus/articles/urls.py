from django.conf.urls import url, patterns

from stucampus.articles.views import AddView, ModifyView
from stucampus.articles.views import manage
from stucampus.articles.views import del_article, set_important
from stucampus.articles.views import add_category, category


urlpatterns = patterns(
    '',
    url(r'^manage/$', manage, name='manage'),
    url(r'^add/$', AddView.as_view(), name='add'),
    url(r'^modify/$', ModifyView.as_view(), name='modify'),
    url(r'^del_article/$', del_article, name='del_article'),
    url(r'^set_important/$', set_important, name='set_important'),

    url(r'^category/$', category, name='category'),
    url(r'^add_category/$', add_category, name='add_category'),
)
