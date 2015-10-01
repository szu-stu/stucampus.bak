# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.core.paginator import InvalidPage, Paginator
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.db.models import Q

from stucampus.dreamer.models import Register
from stucampus.dreamer.forms import Register_Form
from stucampus.account.permission import check_perms


def signup_mobile(request):
    return render(request, 'dreamer/apply_mobile.html',
                  {'form': Register_Form()})


class SignUp(View):
    def get(self, request):
        if request.META['HTTP_USER_AGENT'].lower().find('mobile') > 0:
            return HttpResponseRedirect('/dreamer/mobile/')
        else:
            return render(request, 'dreamer/apply.html',
                          {'form': Register_Form()})

    def post(self, request):
        msg = Register()
        tmp = Register_Form(request.POST)
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            msg.ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            msg.ip = request.META['REMOTE_ADDR']
        msg.status = True
        now = datetime.date.today()
        if tmp.is_valid():
            msg.name = tmp.cleaned_data['name']
            msg.gender = tmp.cleaned_data['gender']
            msg.stu_ID = tmp.cleaned_data['stu_ID']
            msg.college = tmp.cleaned_data['college']
            msg.mobile = tmp.cleaned_data['mobile']
            msg.dept1 = tmp.cleaned_data['dept1']
            msg.dept2 = tmp.cleaned_data['dept2']
            msg.self_intro = tmp.cleaned_data['self_intro']
            same_SID = (Register.objects
                                .filter(stu_ID=msg.stu_ID, status=True)
                                .count())
            if same_SID > 0:
                print "1"
                return render(request, 'dreamer/failed.html')
            else:
                if (Register.objects
                            .filter(sign_up_date=now)
                            .filter(ip=msg.ip).count() >= 50):
                    tip = ("您当前IP已于同一天成功报名五十次，"
                           "请等候第二天或换另一台电脑再进行报名")
                    return render(request, 'dreamer/failed.html', {'tip': tip})
                else:
                    msg.save()
                    return render(request, 'dreamer/succeed.html',
                                  {'form': msg})
        else:

            return render(request, 'dreamer/failed.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'dreamer/index.html')


class CheckMsg(View):

    def get(self, request):
        return render(request, 'dreamer/check_msg.html')

    def post(self, request):
        search = req.POST['search']
        crit = Q(name=search) | Q(stu_ID=search) & Q(status=True)
        objects = Register.objects.filter(crit).count()
        if objects > 0:
            return HttpResponse("已报名成功")
        else:
            return HttpResponse("尚未进行报名或报名不成功，若有疑问请在群里反映.")


def succeed(request):
    return render(request, 'dreamer/succeed.html')


def check(request):
    count = Register.objects.all().count()
    return HttpResponse(count)


@check_perms('dreamer.manager')
def alldetail(request):
    aall = Register.objects.filter(status=True)
    user = request.user

    cbb1 = aall.filter(dept1="cbb")
    cbb2 = aall.filter(dept2="cbb")
    cbbb = (cbb1.filter(gender="male").count()
            + cbb2.filter(gender="male").count())
    cbbg = (cbb1.filter(gender="female").count()
            + cbb2.filter(gender="female").count())

    jsb1 = aall.filter(dept1="jsb")
    jsb2 = aall.filter(dept2="jsb")
    jsbb = (jsb1.filter(gender="male").count()
            + jsb2.filter(gender="male").count())
    jsbg = (jsb1.filter(gender="female").count()
            + jsb2.filter(gender="female").count())

    sjb1 = aall.filter(dept1="sjb")
    sjb2 = aall.filter(dept2="sjb")
    sjbb = (sjb1.filter(gender="male").count()
            + sjb2.filter(gender="male").count())
    sjbg = (sjb2.filter(gender="female").count()
            + sjb1.filter(gender="female").count())

    xzb1 = aall.filter(dept1="xzb")
    xzb2 = aall.filter(dept2="xzb")
    xzbb = (xzb1.filter(gender="male").count()
            + xzb2.filter(gender="male").count())
    xzbg = (xzb1.filter(gender="female").count()
            + xzb2.filter(gender="female").count())

    yyb1 = aall.filter(dept1="yyb")
    yyb2 = aall.filter(dept2="yyb")
    yybb = (yyb1.filter(gender="male").count()
            + yyb2.filter(gender="male").count())
    yybg = (yyb1.filter(gender="female").count()
            + yyb2.filter(gender="female").count())

    return render(request, 'dreamer/situation.html',
                  {"jsb1": jsb1.count(),
                   "jsb2": jsb2.count(),
                   "jsbb": jsbb,
                   "jsbg": jsbg,
                   "sjb1": sjb1.count(),
                   "sjb2": sjb2.count(),
                   "sjbb": sjbb,
                   "sjbg": sjbg,
                   "xzb1": xzb1.count(),
                   "xzb2": xzb2.count(),
                   "xzbb": xzbb,
                   "xzbg": xzbg,
                   "yyb1": yyb1.count(),
                   "yyb2": yyb2.count(),
                   "yybb": yybb,
                   "yybg": yybg,
                   "cbb1": cbb1.count(),
                   "cbb2": cbb2.count(),
                   "cbbb": cbbb,
                   "cbbg": cbbg,
                   "all": aall.count(),
                   "user": user})


@check_perms('dreamer.manager')
def alllist(request):
    applyall = Register.objects.filter(status=True).order_by('sign_up_date')
    paginator = Paginator(applyall, 8)
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except InvalidPage:
        page = paginator.page(1)
    return render(request, 'dreamer/list.html', {'page': page})


@check_perms('dreamer.manager')
def delete(request):
    apply_id = request.GET.get('id')
    app = Register.objects.get(id=apply_id)
    app.status = False
    app.save()
    return HttpResponseRedirect('/dreamer/manage/')


@check_perms('dreamer.manager')
def search(request):
    search = request.GET.get('search')
    app = Register.objects.filter(status=True).filter(name__contains=search)
    if not app:
        if search.isdigit():
            app = Register.objects.filter(status=True).filter(stu_ID=search)
    paginator = Paginator(app, 8)
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except InvalidPage:
        page = paginator.page(1)
    return render(request, 'dreamer/list.html', {'page': page})


@check_perms('dreamer.manager')
def detail(request):
    apply_id = request.GET.get('id')
    app = Register.objects.get(id=apply_id)
    return render(request, 'dreamer/detail.html', {'app': app})


@check_perms('dreamer.manager')
def modify(request):
    apply_id = request.POST['id']
    a = Register.objects.get(id=apply_id)
    a.name = request.POST['name']
    gender = request.POST['sex']
    if gender == u'男':
        a.gender = 'male'
    elif gender == u'女':
        a.gender = 'female'
    a.stu_ID = request.POST['stu_id']
    a.college = request.POST['college']
    a.mobile = request.POST['mobile']
    if request.POST['desired_dept_1'] == u'行政部':
        a.dept1 = 'xzb'
    if request.POST['desired_dept_1'] == u'设计部':
        a.dept1 = 'sjb'
    if request.POST['desired_dept_1'] == u'技术部':
        a.dept1 = 'jsb'
    if request.POST['desired_dept_1'] == u'采编部':
        a.dept1 = 'cbb'
    if request.POST['desired_dept_1'] == u'运营部':
        a.dept1 = 'yyb'
    if request.POST['desired_dept_2'] == u'行政部':
        a.dept2 = 'xzb'
    if request.POST['desired_dept_2'] == u'设计部':
        a.dept2 = 'sjb'
    if request.POST['desired_dept_2'] == u'技术部':
        a.dept2 = 'jsb'
    if request.POST['desired_dept_2'] == u'采编部':
        a.dept2 = 'cbb'
    if request.POST['desired_dept_2'] == u'运营部':
        a.dept2 = 'yyb'
    a.self_intro = request.POST['introduce']
    a.save()
    return HttpResponseRedirect('/dreamer/manage/detail/?id='+apply_id)
