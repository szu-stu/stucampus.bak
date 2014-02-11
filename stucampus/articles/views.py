#-*- coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.paginator import InvalidPage, Paginator

from stucampus.articles.forms import ArticleForm, CategoryForm
from stucampus.articles.forms import CategoryFormset
from stucampus.articles.models import Article, Category
from stucampus.utils import get_client_ip 


NO_CATEGORY = u'未分类'


def create_page(request, include_deleted=False):
    category = request.GET.get('category')
    if not category:
        article_list = Article.objects.all()
    else:
        if category == NO_CATEGORY:
            category = None
        else:
            category = get_object_or_404(Category, name=category)
        article_list = Article.objects.filter(category=category)
    if not include_deleted:
        article_list = article_list.filter(deleted=False)
    paginator = Paginator(article_list, 4)
    try:
        page = paginator.page(request.GET.get('page'))
    except InvalidPage:
        page = paginator.page(1)
    return page


def manage(request):
    page = create_page(request)
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
        article = get_object_or_404(Article, pk=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/article-form.html',
                {'form': form, 'article_id': article_id,
                 'post_url': reverse('articles:modify')})

    def post(self, request):
        article_id = request.GET.get('id')
        article = get_object_or_404(Article, pk=article_id)
        form = ArticleForm(request.POST, instance=article)
        if not form.is_valid():
            return render(request, 'articles/article-form.html',
                {'form': form, 'article_id': article_id,
                 'post_url': reverse('articles:modify')})
        form.save()
        return HttpResponseRedirect(reverse('articles:manage'))


def del_article(request):
    article_id = request.GET.get('id')
    article = get_object_or_404(Article, pk=article_id)
    article.deleted = not article.deleted
    article.save()
    return HttpResponseRedirect(reverse('articles:manage'))


def set_important(request):
    article_id = request.GET.get('id')
    article = get_object_or_404(Article, pk=article_id)
    article.important = not article.important
    article.save()
    return HttpResponseRedirect(reverse('articles:manage'))


class CategoryView(View):

    @staticmethod
    def create_category_list():
        category_list = Category.objects.all()
        category_list = {category.name: \
                len(Article.objects.filter(category=category)) \
                for category in Category.objects.all()}
        category_list[NO_CATEGORY] = \
                len(Article.objects.filter(category=None))
        return category_list

    def get(self, request):
        category_list = CategoryView.create_category_list()
        formset = CategoryFormset()
        return render(request, 'articles/category-form.html',
                {'formset': formset, 'category_list': category_list})

    def post(self, request):
        formset = CategoryFormset(request.POST)
        if not formset.is_valid():
            category_list = CategoryView.create_category_list()
            return render(request, 'articles/category-form.html',
                    {'formset': formset, 'category_list': category_list})
        formset.save()
        return HttpResponseRedirect(reverse('articles:category'))


def article_list(request):
    page = create_page(request)
    category = request.GET.get('category')
    if not category:
        raise Http404
    hot_articles_list = \
        Article.objects.filter(deleted=False).order_by('click_count')[:10]
    newest_articles_list = \
        Article.objects.filter(deleted=False).order_by('-pk')[:10]
    return render(request, 'articles/article-list.html',
            {'page': page, 'category': category,
             'hot_articles_list': hot_articles_list,
             'newest_articles_list': newest_articles_list})


def article_display(request):
    article_id = request.GET.get('id')
    article = get_object_or_404(Article, pk=article_id)
    article.click_count += 1
    article.save()
    return render(request, 'articles/article-display.html',
            {'article': article})

