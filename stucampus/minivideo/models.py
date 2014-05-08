#-*- coding: utf-8
from django.db import models


def save_path(instance, filename):
    return os.path.join('minivideo', 'cover', filename)


class Resource(models.Model):
    
    team_name = models.CharField(max_length=20)
    team_captain = models.CharField(max_length=None)
    team_members = models.CharField(max_length=None)
    team_psw = models.CharField(max_length=30)
    team_cover = preview1 = models.ImageField(upload_to=save_path, blank=False)
    video_name = models.CharField(max_length=50)
    video_intro = models.CharField(max_length=200)
    video_link = models.URLField(max_length=100)
    votes = models.IntegerField(default=0)
    has_verified = models.BooleanField(default=False)

