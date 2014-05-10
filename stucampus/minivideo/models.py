#-*- coding: utf-8
import os

from django.db import models


def save_path(instance, filename):
    return os.path.join('minivideo', 'cover', filename)


class Resource(models.Model):
    
    class Meta:
        permissions = (
            ('manager', u'微视大赛管理员'),
        )

    team_captain = models.CharField(max_length=20)
    team_captain_phone = models.CharField(max_length=30)
    team_captain_stuno = models.CharField(max_length=10)
    team_captain_college = models.CharField(max_length=30)    
    team_members1_name = models.CharField(max_length=20, blank=True)
    team_members1_id = models.CharField(max_length=10, blank=True)
    team_members2_name = models.CharField(max_length=20, blank=True)
    team_members2_id = models.CharField(max_length=10, blank=True)
    team_members3_name = models.CharField(max_length=20, blank=True)
    team_members3_id = models.CharField(max_length=10, blank=True)
    team_members4_name = models.CharField(max_length=20, blank=True)
    team_members4_id = models.CharField(max_length=10, blank=True)
    team_members5_name = models.CharField(max_length=20, blank=True)
    team_members5_id = models.CharField(max_length=10, blank=True)
    team_psw = models.CharField(max_length=30)
    video_cover = models.ImageField(upload_to=save_path)
    video_name = models.CharField(max_length=50)
    video_intro = models.CharField(max_length=200)
    video_link = models.URLField(max_length=150)
    votes = models.IntegerField(default=0)
    has_verified = models.BooleanField(default=False)

