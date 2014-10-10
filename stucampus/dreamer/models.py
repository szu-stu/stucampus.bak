#-*- coding: utf-8 -*-
from django.db import models


class Application(models.Model):

    SEX = (
        ('boy', u'男'),
        ('girl', u'女'),
    )

    stu_num = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=5, choices=SEX)
    college = models.CharField(max_length=30)
    apply_date = models.DateTimeField(auto_now=True)
    fav_sports = models.CharField(max_length=30)
    interest = models.CharField(max_length=30)
    self_intro = models.CharField(max_length=200)
