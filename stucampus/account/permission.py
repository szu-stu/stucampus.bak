#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth import REDIRECT_FIELD_NAME

from stucampus.utils import spec_json


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
                              messages=messages)
            return fucntion(request, *args, **kwargs)
        return wrapped_check
    return decorator


def check_admin(function):
    def wrapped_check(request, *args, **kwargs):
        try:
            admin_group = Group.objects.get(name='StuCampus')
        except Group.DoesNotExist:
            return render(request, 'master/deny.html',
                          messages=u'StuCampus组织未创建')
        if not admin_group in request.user.groups.all():
            return render(request, 'master/deny.html',
                          messages=u'非网站管理员')
        return function(request, *args, **kwargs)
    return wrapped_check
