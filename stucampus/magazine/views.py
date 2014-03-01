#-*- coding: utf-8
import os

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.paginator import InvalidPage, Paginator
from stucampus.account.permission import check_perms
from django.utils.decorators import method_decorator

from stucampus.magazine.models import Magazine
from stucampus.magazine.forms import MagazineForm 


MAGAZINE_NAME = {
        'szuyouth': u'深大青年',
        'langtaosha': u'浪淘沙',
        }


def magazine_list(request, name):
    maga_list = Magazine.objects. \
            filter(name=MAGAZINE_NAME[name]).order_by('-pk')
    if not magazine_list:
        raise Http404
    return render(request, 'magazine/list.html', {'list': maga_list})


def display(request, id):
    magazine = get_object_or_404(Magazine, id=id)
    pdfjs_url = os.path.join('/', 'pdfjs', 'web', 'viewer.html')
    pdf_path = os.path.join('/', 'media', str(magazine.pdf_file))
    return HttpResponseRedirect(pdfjs_url + '?file=' + pdf_path)


@check_perms('magazine.magazine_add')
def manage(request):
    maga_list = Magazine.objects.all().order_by('-pk')
    return render(request, 'magazine/manage.html', {'list': maga_list})


class AddView(View):
    @method_decorator(check_perms('magazine.magazine_add'))
    def get(self, request):
        form = MagazineForm()
        return render(request, 'magazine/magazine-form.html',
                {'form': form, 'post_url': reverse('magazine:add')})

    @method_decorator(check_perms('magazine.magazine_add'))
    def post(self, request):
        form = MagazineForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'magazine/magazine-form.html',
                    {'form': form, 'post_url': reverse('magazine:add')})
        form.save()
        return HttpResponseRedirect(reverse('magazine:manage'))


class ModifyView(View):
    @method_decorator(check_perms('magazine.magazine_modify'))
    def get(self, request):
        maga_id = request.GET.get('id')
        magazine = get_object_or_404(Magazine, id=maga_id)
        form = MagazineForm(instance=magazine)
        return render(request, 'magazine/magazine-form.html',
                {'form': form,
                 'post_url': reverse('magazine:modify') + '?id=' + maga_id})

    @method_decorator(check_perms('magazine.magazine_modify'))
    def post(self, request):
        maga_id = request.GET.get('id')
        magazine = get_object_or_404(Magazine, id=maga_id)
        form = MagazineForm(request.POST, request.FILES, instance=magazine)
        if not form.is_valid():
            return render(request, 'magazine/magazine-form.html',
                    {'form': form,
                     'post_url': reverse('magazine:modify') + '?id=' + maga_id})
        form.save()
        return HttpResponseRedirect(reverse('magazine:manage'))


