from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'stucampus.master.views.admin.redirect', name='admin_index'),
    
    url(r'^status$',
        'stucampus.master.views.admin.status', name='admin_status'),
    
    url(r'^organizations$',
        'stucampus.master.views.admin.organizations',
        name='admin_organization'),
    url(r'^organization/(?P<id>\d+)$',
        'stucampus.master.views.admin.organization_operate',
        name='admin_organization_operate'),
    url(r'^organization/(?P<id>\d+)/manager$',
        'stucampus.master.views.admin.organization_manager',
        name='admin_organization_manager'),
    
    url(r'^accounts$',
        'stucampus.master.views.admin.account',
        name='admin_accounts'),
    url(r'^account/(?P<id>\d+)$',
        'stucampus.master.views.admin.account_operate',
        name='admin_account_operate'),
    
    url(r'^organization$',
        'stucampus.organization.views.organization_manage',
        name='organization_manage'),
    url(r'^organization/(?P<id>\d+)/edit$',
        'stucampus.organization.views.organization_edit',
        name='organization_edit'),
)