# -*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.paginator import InvalidPage

from stucampus.activity.models import ActivityMessage
from stucampus.activity.forms import ActivityMessageForm
from stucampus.activity.forms import ActivityMessageFormSet
from stucampus.custom.forms_utils import FormsetPaginator


def index(request):
    table = ActivityMessage.generate_messages_table()
    return render_to_response('activity/home.html', {'table': table})


class ManageView(generic.View):

    @classmethod
    def __create_page(cls, request):
        paginator = FormsetPaginator(ActivityMessage,
                                     ActivityMessage.objects.all(), 5,
                                     formset=ActivityMessageFormSet)
        try:
            page = paginator.page(request.GET.get('page'))
        except InvalidPage:
            page = paginator.page(1)
        return page
   
    def get(self, request):
        return render(request, 'activity/manage.html',
                      {'page': ManageView.__create_page(request)})
    
    def post(self, request):
        formset = ActivityMessageFormSet(request.POST)
        if not formset.is_valid():
            page = ManageView.__create_page(request)
            page.formset = formset
            return render(request, 'activity/manage.html',
                          {'page': page})
        # 当extra>0的时候，不能循环form来save()
        formset.save()
        page = request.GET.get('page')
        return HttpResponseRedirect(
                reverse('activity:manage')+('?page='+page if page else ''))

