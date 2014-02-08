from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.paginator import InvalidPage, Paginator

from stucampus.articles.forms import ArticleForm, CategoryForm
from stucampus.articles.models import Article, Category
from stucampus.utils import get_client_ip 


def manage(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 4)
    try:
        page = paginator.page(request.GET.get('page'))
    except InvalidPage:
        page = paginator.page(1)
    return render(request, 'articles/manage.html',
            {'page': page})


class AddView(View):

    def get(self, request):
        form = ArticleForm()
        return render(request, 'articles/article-form.html',
                {'form': form, 'post_url': reverse('articles:add')})

    def post(self, request):
        form = ArticleForm(request.POST)
        if not form.is_valid():
            return render(request, 'articles/article-form.html',
                    {'form': form, 'post_url': reverse('articles:add')})
        article = form.save(commit=False)
        article.editor = request.user
        article.create_ip = get_client_ip(request)
        article.save()
        return HttpResponseRedirect(reverse('articles:manage'))


class ModifyView(View):

    def get(self, request):
        article_id = request.GET.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/article-form.html',
                {'form': form, 'article_id': article_id,
                 'post_url': reverse('articles:modify')})

    def post(self, request):
        article_id = request.GET.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if not form.is_valid():
            return render(request, 'articles/article-form.html',
                {'form': form, 'article_id': article_id,
                 'post_url': reverse('articles:modify')})
        form.save()
        return HttpResponseRedirect(reverse('articles:manage'))


def del_article(request):
    article_id = request.GET.get('id')
    article = Article.objects.get(id=article_id)
    article.deleted = not article.deleted
    article.save()
    return HttpResponseRedirect(reverse('articles:manage'))


def set_important(request):
    article_id = request.GET.get('id')
    article = Article.objects.get(id=article_id)
    article.important = not article.important
    article.save()
    return HttpResponseRedirect(reverse('articles:manage'))


def category(request):
    category_list = Category.objects.all()
    form = CategoryForm()
    return render(request, 'articles/category-form.html',
            {'form': form, 'category_list': category_list})


def add_category(request):
    form = CategoryForm(request.POST)
    if not form.is_valid():
        return render(request, 'articles/category-form.html',
                {'form': form})
    article = form.save()
    return HttpResponseRedirect(reverse('articles:category'))


def change_priority(request):
    pass
