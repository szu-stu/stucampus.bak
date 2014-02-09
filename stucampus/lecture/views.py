#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from django.core.paginator import InvalidPage

from stucampus.lecture.models import LectureMessage
from stucampus.lecture.forms import LectureForm, LectureFormset
from stucampus.custom.forms_utils import FormsetPaginator


def index(request):
    table = LectureMessage.generate_messages_table()
    return render_to_response('lecture/home.html', {'table': table})


class ManageView(generic.View):

    @classmethod
    def __create_page(cls, request):
        paginator = FormsetPaginator(LectureMessage,
                                     LectureMessage.objects.all(), 5,
                                     formset=LectureFormset)
        try:
            page = paginator.page(request.GET.get('page'))
        except InvalidPage:
            page = paginator.page(1)
        return page
   
    def get(self, request):
        return render(request, 'lecture/manage.html',
                      {'page': ManageView.__create_page(request)})
    
    def post(self, request):
        formset = LectureFormset(request.POST)
        if not formset.is_valid():
            page = ManageView.__create_page(request)
            page.formset = formset
            return render(request, 'lecture/manage.html',
                          {'page': page})
        # 当extra>0的时候，不能循环form来save()
        formset.save()
        page = request.GET.get('page')
        return HttpResponseRedirect(
                reverse('lecture:manage')+('?page='+page if page else ''))

