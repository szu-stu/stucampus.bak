from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from django.core.paginator import InvalidPage

from stucampus.utils import spec_json
from stucampus.lecture.models import LectureMessage
from stucampus.lecture.forms import LectureForm, LecureFormSet
from stucampus.activity.forms import FormsetPaginator


def index(request):
    table = LectureMessage.generate_messages_table()
    return render_to_response('lecture/index.html', {'table': table})


def manage(request, page_num='1'):
    queryset = LectureMessage.get_messages_this_week()
    paginator = FormsetPaginator(LectureMessage, queryset, 2)
    try:
        page = paginator.page(int(page_num))
    except InvalidPage:
        page = paginator.page(1)
    return render(request, 'lecture/manage.html', {'page': page})


def submit(request):
    formset = LecureFormSet(request.POST)
    for form in formset:
        if form.is_valid():
            lecture_message = form.save(commit=False)
            lecture_message.url_id = lecture_message.url_id_backup
            lecture_message.save()
    return HttpResponseRedirect(reverse('lecture:manage'))


def add_lecture(request):
    form = LectureForm()
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            lecture_message = form.save(commit=False)
            lecture_message.url_id_backup = lecture_message.url_id
            lecture_message.save()
            return HttpResponseRedirect(reverse('lecture:manage'))
        else:
            return spec_json(False, form.errors)
    return render(request, 'lecture/add_lecture.html', {'form': form})


# just used for debug
def delete(request):
    LectureMessage.objects.all().delete()
    return HttpResponseRedirect(reverse('lecture:manage'))
