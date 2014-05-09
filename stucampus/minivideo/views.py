from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from stucampus.minivideo.models import Resource
from stucampus.minivideo.forms import SignUpForm, CommitForm

class SignUpView(View):
    def get(self, request):
        resource_id = request.GET.get('id')        
        if resource_id is None:
            form = SignUpForm()
	    flag = False
            return render(request, 'minivideo/signup.html', {'form':form,'flag':flag})
	flag = True
        resource = get_object_or_404(Resource, pk=resource_id)
        form = CommitForm(instance=resource)
        return render(request, 'minivideo/signup.html', {'form':form,'flag':flag})

    def post(self, request):
        resource_id = request.GET.get('id')        
        if resource_id is None:
            form = SignUpForm(request.POST)
            if not form.is_valid():
                return render(request, 'minivideo/signup.html', {'form':form})
            form.save()
            return render(request, 'minivideo/list.html')
        resource = get_object_or_404(Resource, pk=resource_id)
        form = CommitForm(instance=resource)
        if not form.is_valid():
        	return render(request, 'minivideo/signup.html', {'form':form})
        form.save()
        return render(request, 'minivideo/list.html')

def resource_list(request):
    resources = Resource.objects.all().order_by('has_verified','id')
    page = request.GET.get('page')
    paginator = Paginator(resources,15)
    try:
        page_list = paginator.page(page)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)

    return render(request,'minivideo/list.html',{ 'page_list':page_list})
