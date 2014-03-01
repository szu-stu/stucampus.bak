#-*- coding: utf-8
import platform

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from stucampus.custom.permission import admin_group_check
from stucampus.account.permission import check_perms


def redirect(request):
    return HttpResponseRedirect('/manage/status')


@check_perms('account.website_admin')
def status(request):
    python_version = platform.python_version()
    domain = request.get_host()
    param = {'python_version': python_version,
             'domain': domain}
    return render(request, 'master/status.html', param)
