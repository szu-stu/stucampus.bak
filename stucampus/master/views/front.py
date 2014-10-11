# -*- coding: utf-8
from django.shortcuts import render

from stucampus.articles.models import Article, Category
from stucampus.lecture.models import LectureMessage
from stucampus.activity.models import ActivityMessage


def generate_category(category):
    return (category,
            Article.objects.filter(
                publish=True,
                deleted=False,
                category=object).order_by('-pk')[:5])


def index(request):
    # 深大焦点
    important_articles = (Article.objects
                          .filter(publish=True, deleted=False, important=True)
                          .order_by('-pk')[:3])
    # 不同类别的文章
    all_cagetory = Category.objects.order_by('priority').all()
    article_dict = (generate_category(category)
                    for category in all_cagetory)

    lecture_list = (LectureMessage.objects
                    .filter(checked=True).order_by('-pk')[:7])
    activity_list = (ActivityMessage.objects
                     .filter(checked=True).order_by('-pk')[:7])
    return render(request, "index.html",
                  {'important_articles': important_articles,
                   'article_dict': article_dict,
                   'lecture_list': lecture_list,
                   'activity_list': activity_list})


def about_us(request):
    return render(request, "aboutus.html")


def page_not_found(request):
    return render(request, "404.html")
