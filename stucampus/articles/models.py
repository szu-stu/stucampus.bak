#-*- coding: utf-8
from django.db import models
from django.contrib.auth.models import User

from DjangoUeditor.models import UEditorField

from stucampus.custom.models_utils import file_save_path


class Category(models.Model):
    name = models.CharField(max_length=30)
    priority = models.PositiveIntegerField()


class Article(models.Model):

    class Meta:
        permissions = (
            ('article_add', u'添加文章'),
            ('article_modify', u'编辑文章'),
            ('article_post', u'发布文章'),
        )

    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=50, blank=True, null=True)
    content = UEditorField(height=500, width=700, toolbars='mini')
    category = models.CharField(max_length=30)

    author = models.CharField(max_length=30)
    editor = models.ForeignKey(User)
    source = models.CharField(max_length=50, blank=True, null=True)
    source_link = models.URLField(blank=True, null=True)
    cover = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    create_ip = models.IPAddressField(editable=False)
    click_count = models.IntegerField(default=0, editable=False)
    deleted = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

