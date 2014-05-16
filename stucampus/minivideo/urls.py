from django.conf.urls import patterns, include, url

from .views import SignUpView,resource_list,verify,details,index,resource_delete
urlpatterns = patterns('',
    url(r'^signup$', SignUpView.as_view(), name='signup'),
    url(r'^list$', resource_list, name='resource_list'),
    url(r'^verify$', verify, name='verify'),
    url(r'^$', index, name='index'),
    url(r'^details$', details, name='details'),
    url(r'^delete$',resource_delete,name="delete")
    
)
