from django.conf.urls import url, patterns

from stucampus.dreamer.views import (index, SignUp, signup_mobile,
                                     CheckMsg, succeed, alldetail,
                                     alllist, delete, search, modify)


urlpatterns = patterns(
    '',
    url(r'index$', index, name='index'),
    url(r'^signup/$', SignUp.as_view(), name='signup'),
    url(r'^mobile/$', signup_mobile, name='mobile'),
    url(r'^check_msg/$', CheckMsg.as_view(), name='check'),
    url(r'^succeed/$', succeed, name='succeed'),
    url(r'^sunup/$', alldetail, name='sunup'),
    url(r'^manage/$', alllist, name='list'),
    url(r'^manage/delete/$', delete, name='delete'),
    url(r'^manage/search/$', search, name='search'),
    url(r'^manage/modify/$', modify, name='modify'),
)
