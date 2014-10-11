# -*- coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def redirect(request):
    return HttpResponseRedirect('/manage/index')


@login_required
def index(request):
    return render(request, 'master/index.html')
