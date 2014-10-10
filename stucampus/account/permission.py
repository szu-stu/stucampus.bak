# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from stucampus.organization.model import Organization


def guest_or_redirect(function=None):
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated(),
        login_url='/',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def check_perms(perm, message=u'无权限'):
    ''' accustomed version of permission_required '''
    def decorator(function):
        def wrapped_check(request, *args, **kwargs):
            if not isinstance(perm, (list, tuple)):
                perms = (perm, )
            else:
                perms = perm
            if not request.user.has_perms(perms):
                return render(request, 'master/deny.html',
                              {'message': message})
            return function(request, *args, **kwargs)
        return wrapped_check
    return decorator


def check_org_manager(function):
    def wrapped_check(request, *args, **kwargs):
        ''' require id indicating organization in url '''
        try:
            org = Organization.objects.get(id=id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(u'id对应的组织不存在')
        if request.user.student not in org.managers.all():
            return render(request, 'master/deny.html',
                          {'message': u'非%s的管理员' % org.name})
        return function(request, *args, **kwargs)
    return wrapped_check
