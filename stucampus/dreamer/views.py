from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View

from .models import Application
from .forms import AppForm


class ApplyView(View):

    def get(self, request):
        return render(request, 'dreamer/loading.html', {'form': AppForm()})

    def post(self, request):
        form = AppForm(request.POST)
        if not form.is_valid():
            return render(request, 'dreamer/loading.html',
                          {'form': form})
        form.save()
        return HttpResponseRedirect(reverse('dreamer:index'))


def manage_list(request):
    app = Application.objects.all().order_by('apply_date')
    paginator = Paginator(app, 6)
    page = request.GET.get('page')

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'dreamer/manage-list.html', {'page': page})


def app_view(request):
    app_id = request.GET.get('id')
    app = get_object_or_404(Application, id=app_id)
    return render(request, 'dreamer/view.html', {'app': app})
