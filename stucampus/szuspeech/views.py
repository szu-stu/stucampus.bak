from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.db.models import Q

from stucampus.szuspeech.models import Resource
from stucampus.szuspeech.forms import  ResourceForm 


def index(request):
    search = request.GET.get('search')
    if search is None:
        resource_list = Resource.objects.all().order_by('-is_top','-published_date')
    else:
        searches = search.strip().split()
        multiSearch = Q()
        for key in searches:
            multiSearch = multiSearch|Q(resource_title__icontains=key)
        resource_list = Resource.objects.filter(multiSearch).order_by('-is_top','-published_date')

    page = request.GET.get('page')
    paginator = Paginator(resource_list,10)
    try:
        page_list = paginator.page(page)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)

    return render(request,'szuspeech/index.html',{ 'page_list':page_list,'search':search})


def manage_list(request):
    resources = Resource.objects.all().order_by('-is_top','-published_date')
    paginator = Paginator(resources, 6)
    page = request.GET.get('page')
     
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    return render(request, 'szuspeech/manage-list.html', {'page': page})


def del_resource(request):
    resource_id = request.GET.get('id')
    resource = get_object_or_404(Resource, pk=resource_id)
    resource.delete()
    return HttpResponseRedirect(reverse('szuspeech:manage_list'))


def set_top(request):
    resource_id = request.GET.get('id')
    resource = get_object_or_404(Resource, pk=resource_id)
    Resource.objects.filter(pk=resource_id).update(is_top=not resource.is_top)
    return HttpResponseRedirect(reverse('szuspeech:manage_list'))


class AddResourceView(View):
    def post(self, request):
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("szuspeech:manage_list"))
        return render(request, 'szuspeech/manage-form.html', {'form':form})

    def get(self, request):
        form = ResourceForm()
        return render(request, 'szuspeech/manage-form.html', {'form':form})


class ModifyResorceView(View):
    def post(self, request):
        resource_id = request.GET.get('id')
        resource = get_object_or_404(Resource, pk=resource_id)
        form = ResourceForm(request.POST,request.FILES,instance=resource)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("szuspeech:manage_list"))
        return render(request,'szuspeech/manage-form.html',{'form':form})

    def get(self, request):
        resouce_id = request.GET.get('id')
        resource = get_object_or_404(Resource, id=resouce_id)
        form = ResourceForm(instance=resource)
        return render(request, 'szuspeech/manage-form.html', {'form':form})