#-*- coding: utf-8
from django.db import models


def save_path(instance, filename):
    return os.path.join('minivideo', 'cover', filename)


class Resource(models.Model):
    
    team_captain = models.CharField(max_length=12)
    team_captain_phone = models.CharField(max_length=11)
    team_captain_stuno = models.CharField(max_length=10)
    team_captain_college = models.CharField(max_length=12)    
    team_members1_name = models.CharField(max_length=12, blank=True)
    team_members1_id = models.CharField(max_length=10, blank=True)
    team_members2_name = models.CharField(max_length=12, blank=True)
    team_members2_id = models.CharField(max_length=10, blank=True)
    team_members3_name = models.CharField(max_length=12, blank=True)
    team_members3_id = models.CharField(max_length=10, blank=True)
    team_members4_name = models.CharField(max_length=12, blank=True)
    team_members4_id = models.CharField(max_length=10, blank=True)
    team_members5_name = models.CharField(max_length=12, blank=True)
    team_members5_id = models.CharField(max_length=10, blank=True)
    team_psw = models.CharField(max_length=30)
    video_cover = models.ImageField(upload_to=save_path, blank=True)
    video_name = models.CharField(max_length=50, blank=True)
    video_intro = models.CharField(max_length=200, blank=True)
    video_link = models.URLField(max_length=100, blank=True)
    votes = models.IntegerField(default=0)
    has_verified = models.BooleanField(default=False)

