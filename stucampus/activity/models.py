# -*- coding:utf-8 -*-
from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone


MORNING = u'上午'
AFTERNOON = u'下午'


class ActivityMessage(models.Model):

    TIME = (
        (MORNING, MORNING),
        (AFTERNOON, AFTERNOON),
        )

    title = models.CharField(max_length=30)
    date= models.DateTimeField()
    time = models.CharField(max_length=10, choices=TIME)
    specific_time = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    summary = models.CharField(max_length=140)

    modified_date_time = models.DateTimeField(editable=False, auto_now=True) 
    checked = models.BooleanField(default=False)

    @classmethod
    def get_activity_list(cls):
        return cls.objects.filter(date_time__gte=timezone.now())

    @classmethod
    def generate_messages_table(cls):
        message_table = cls.create_empty_table()
        message_table = cls.fill_in_table(message_table)
        return message_table

    @staticmethod
    def create_empty_table():
        message_table = {}
        message_table['date'] = []
        message_table['morning'] = []
        message_table['afternoon'] = []
        now = timezone.now()
        date_of_this_Monday = now - timedelta(days=now.weekday())
        for i in range(0, 7):
            date = date_of_this_Monday + timedelta(days=i)
            message_table['date'].append(date)
            message_table['morning'].append([])
            message_table['afternoon'].append([])
        return message_table

    @staticmethod
    def fill_in_table(message_table):
        messages_this_week = ActivityMessage.get_messages_this_week()
        to_be_published = messages_this_week.filter(checked=True)
        for msg in to_be_published:
            if msg.date == MORNING:
                message_table['morning'][msg.date.weekday()].append(msg)
            else:
                message_table['afternoon'][msg.date.weekday()].append(msg)
        return message_table

    @classmethod
    def get_messages_this_week(cls):
        now = timezone.now()
        date_of_this_Monday = now - timedelta(days=now.weekday())
        date_of_next_Monday = date_of_this_Monday + timedelta(days=7)
        lecture_held_this_week = cls.objects.filter(

            date__gte=date_of_this_Monday,
            date__lt=date_of_next_Monday)
        return lecture_held_this_week
