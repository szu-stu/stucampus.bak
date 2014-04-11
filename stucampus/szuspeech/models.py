#-*- coding: utf-8
import os

from django.db import models


def save_path(instance, filename):
    return os.path.join('szuspeech', 'upload_file', filename)


def preview_pic_save_path(instance, filename):
    return os.path.join('szuspeech', 'preview_pic', filename)


class Resource(models.Model):

    class Meta:
        permissions = (
            ('manager', u'深大演讲管理员'),
        )

    resource_title = models.CharField(max_length=50)
    resource_intro = models.CharField(max_length=200)
    uploaded_file = models.FileField(upload_to=save_path)
    is_preview =  models.BooleanField(default=False) 
    preview1 = models.ImageField(upload_to=preview_pic_save_path, blank=True)
    preview2 = models.ImageField(upload_to=preview_pic_save_path, blank=True)
    preview3 = models.ImageField(upload_to=preview_pic_save_path, blank=True)
    published_date = models.DateTimeField(auto_now=True)
    is_top = models.BooleanField(default=False)

