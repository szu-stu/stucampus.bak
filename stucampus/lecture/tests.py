# -*- coding: utf-8 -*-
from datetime import date, time, datetime

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist

from stucampus.spider.models import Notification
from stucampus.lecture.models import LectureMessage
from stucampus.lecture.implementation import update_lecture_from_notification


class ParseTest(TestCase):

    def test_update(self):
        title = u'土木工程学院可持续性建设学术沙龙系列讲座'
        content = u'''题 目：Strategies for improving the quality, quantity and citation impacts of your research/journal papers
主 讲：Professor Patrick, X.W. Zou, PhD, UNSW,

Chair of Building and Construction Management, Faculty of Business, Government & Law, Fellow of ANZSOG Institute for Governance, University of Canberra, AUSTRALIA

时 间：2014-1-13 (星期一下午)，14:00-16:00
地 点：深圳大学南区土木工程学院院馆B401室
语 言：English+Chinese '''
        noti = Notification(url_id=600600,
                            title=title,
                            published_date=datetime.now(),
                            category=u'学术',
                            publisher='doyoubi',
                            content=content)
        # test this function
        update_lecture_from_notification([noti])
        lecture_msg = LectureMessage.objects.get(url_id=600600)
        self.assertEqual(lecture_msg.title,
                u'Strategies for improving the quality, quantity and citation impacts of your research/journal papers')
        self.assertEqual(lecture_msg.date, date(2014, 1, 13))
        self.assertEqual(lecture_msg.time, u'下午')
        self.assertEqual(lecture_msg.place,
                u'深圳大学南区土木工程学院院馆B401室')
        self.assertEqual(lecture_msg.speaker,
                u'Professor Patrick, X.W. Zou, PhD, UNSW,')

