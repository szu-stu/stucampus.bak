#-*- coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.paginator import InvalidPage, Paginator

from stucampus.magazine.models import Magazine
from stucampus.magazine.forms import MagazineForm 


def magazine_list(request, name):
    maga_list = Magazine.objects.filter(name=name)
    if not magazine_list:
        raise Http404
    return render(request, 'magazine/list.html', {'list': maga_list})


def display(request, name, issue):
    magazine = get_object_or_404(Magazine, name=name, issue=issue)
    return render(request, 'magazine/display.html', {'magazine': magazine})


def manage(request):
    maga_list = Magazine.objects.all()
    return render(request, 'magazine/manage.html', {'list': maga_list})


class AddView(View):
    def get(self, request):
        form = MagazineForm()
        return render(request, 'magazine/magazine-form.html',
                {'form': form, 'post_url': reverse('magazine:add')})

    def post(self, request):
        form = MagazineForm(request.POST)
        if not form.is_valid():
            return render(request, 'magazine/magazine-form.html',
                    {'form': form, 'post_url': reverse('magazine:add')})
        form.save()
        return HttpResponseRedirect(reverse('magazine:manage'))


class ModifyView(View):
    def get(self, request):
        maga_id = request.GET.get('id')
        magazine = get_object_or_404(Magazine, id=maga_id)
        form = MagazineForm(instance=magazine)
        return render(request, 'magazine/magazine-form.html',
                {'form': form,
                 'post_url': reverse('magazine:modify') + '?id=' + maga_id})

    def post(self, request):
        maga_id = request.GET.get('id')
        magazine = get_object_or_404(Magazine, id=maga_id)
        form = MagazineForm(request.POST, instance=magazine)
        if not form.is_valid():
            return render(request, 'magazine/magazine-form.html',
                    {'form': form,
                     'post_url': reverse('magazine:modify') + '?id=' + maga_id})
        form.save()
        return HttpResponseRedirect(reverse('magazine:manage'))


