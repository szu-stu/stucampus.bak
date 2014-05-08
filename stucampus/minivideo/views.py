from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from stucampus.minivideo.models import Resource
from stucampus.minivideo.forms import SignUpForm, CommitForm

class SignUpView(View):
    def get(self, request):
        resource_id = request.GET.get('id')        
        if  resource_id is  None:
            form = SignUpForm()
            return render(request, 'minivideo/signup.html', {'form':form})
        resource = get_object_or_404(Resource, pk=resource_id)
        form = CommitForm(instance=resource)
        return render(request, 'minivideo/signup.html', {'form':form})

    def post(self, request):
        resource_id = request.GET.get('id')        
        if  resource_id is  None:
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
