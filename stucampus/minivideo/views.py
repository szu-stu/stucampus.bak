from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from stucampus.minivideo.models import Resource
from stucampus.minivideo.forms import SignUpForm

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'minivideo/signup.html', {'form':form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'minivideo/signup.html', {'form':form})
        form.save()
        return render(request, 'minivideo/list.html')

