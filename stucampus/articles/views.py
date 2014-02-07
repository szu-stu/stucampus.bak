from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View

from stucampus.articles.forms import ArticleForm
from stucampus.articles.models import Article


def manage(request):
    listing = Article.objects.all()
    return render(request, 'index.html', {'listing': listing})


class PostView(View):

    def get(self, request):
        form = ArticleForm()
        return render(request, 'articles/article-form.html',
                {'form': form, 'post_url': reverse('articles:add')})

    def post(self, request):
        form = ArticleForm(request.POST)
        if not form.is_valid():
            return render(request, 'articles/article-post.html',
                    {'form': form, 'post_url': reverse('articles:add')})
        form.save()
        return HttpResponseRedirect(reverse(''))


class ModifyView(View):

    def get(self, request):
        article_id = request.GET.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/article-form.html',
                {'form': form, 'article_id': article_id,
                 'post_url': reverse('articles:add')})

    def post(self, request):
        article_id = request.GET.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if not form.is_valid():
            return render(request, 'articles/article-form.html',
                {'form': form, 'article_id': article_id,
                 'post_url': reverse('articles:add')})
        form.save()
        return HttpResponseRedirect(reverse(''))
