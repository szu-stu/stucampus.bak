#-*- coding: utf-8
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from stucampus.utils import spec_json, get_client_ip, get_http_data
from stucampus.account.models import Student
from stucampus.account.forms import SignInForm, SignUpForm
from stucampus.account.forms import ProfileEditForm, PasswordForm
from stucampus.account.services import find_by_email, student_is_exist


def sign_in(request):
    if request.user.is_authenticated() and request.method != 'DELETE':
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        form = SignInForm()
        return render(request, 'account/sign-in.html', {'form': form})
    elif request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user.student.login_count = user.student.login_count + 1
                    user.student.last_login_ip = get_client_ip(request)
                    user.student.save()
                    success = True
                    messages = [u'登录成功']
                else:
                    success = False
                    messages = [u'账户停用']
            else:
                # user not found.
                success = False
                messages = [u'邮箱或密码错误']
        else:
            success = False
            messages = form.errors.values()
        return spec_json(success, messages)


def sign_out(request):
    if request.method == 'POST':
        logout(request)
        success = True
        messages = [u'退出成功']
        return spec_json(success, messages)


def sign_up(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'account/sign-up.html', {'form': form})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            confirm = request.POST['confirm']
            if not password == confirm:
                messages = [u'密码不匹配, 请检查后重新输入']
                success = False
            else:
                email_is_exist = student_is_exist(email)
                if email_is_exist:
                    success = False
                    messages = [u'邮箱已存在']
                else:
                    new_user = User.objects.create_user(email, email, password)
                    student = Student.objects.create(user=new_user)
                    student.screen_name = email.split('@')[0]
                    student.last_login_ip = get_client_ip(request)
                    student.save()
                    success = True
                    messages = [u'注册成功']
        else:
            success = False
            messages = form.errors.values()
        return spec_json(success, messages)


def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/signin')
    if request.method == 'GET':
        return render(request, 'account/profile.html')
    elif request.method == 'PUT':
        data = get_http_data(request)
        form = ProfileEditForm(data)
        if form.is_valid():
            user = request.user
            user.student.true_name = data['true_name']
            user.student.college = data['college']
            user.student.screen_name = data['screen_name']
            user.student.is_male = data['is_male']
            user.student.mphone_num = data['mphone_num']
            birthday = data['birthday']
            if len(birthday) > 0:
                user.student.birthday = datetime.strptime(birthday, '%Y-%m-%d')
            user.student.mphone_short_num = data['mphone_short_num']
            user.student.student_id = data['student_id']
            user.student.szucard = data['szucard']
            user.student.save()
            success = True
            messages = [u'修改成功']
        else:
            success = False
            messages = form.errors.values()
        return spec_json(success, messages)


@login_required
def profile_edit(request):
    college_list = Student.COLLEGE_CHOICES
    return render(request, 'account/profile-edit.html',
                  {'college_list': college_list})


@login_required
def password(request):
    if request.method == 'GET':
        return render(request, 'account/password.html')
    elif request.method == 'PUT':
        data = get_http_data(request)
        form = PasswordForm(data)
        if form.is_valid():
            current_user = request.user
            query_user = authenticate(username=current_user.username,
                                      password=data['current_password'])
            if not query_user is None:
                if data['new_password'] == data['confirm']:
                    current_user.set_password(data['confirm'])
                    current_user.save()
                    success = True
                    messages = []
                else:
                    success = False
                    messages = [u'密码不匹配']
            else:
                success = False
                messages = [u'密码错误!']
        else:
            messages = form.errors.values()
            success = False
        return spec_json(success, messages)
