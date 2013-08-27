#-*- coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    COLLEGE_CHOICES = (
        ('SF', '师范学院'), ('WX', '文学院'), ('WGY', '外国语学院'),
        ('CB', '传播学院'), ('JJ', '经济学院'), ('GL', '管理学院'),
        ('FX', '法学院'), ('YS', '艺术设计学院'), ('SK', '社会科学学院'),
        ('SX', '数学与计算科学学院'), ('WL', '物理科学与技术学院'),
        ('HG', '化学与化工学院'), ('CL', '材料学院'), ('XX', '信息工程学院'),
        ('JR', '计算机与软件学院'), ('JG', '建筑与城市规划学院'),
        ('TM', '土木工程学院'), ('DZ', '电子科学与技术学院'),
        ('JD', '机电与控制工程学院'), ('SK', '生命科学学院'),
        ('GD', '光电工程学院'), ('GEF', '高尔夫学院'), ('YXY', '医学院'),
        ('GJ', '国际交流学院'), ('JX', '继续教育学院')
    )

    user = models.OneToOneField(User)
    true_name = models.CharField(max_length=20)
    college = models.CharField(max_length=4, choices=COLLEGE_CHOICES,
                               null=True, blank=True)
    screen_name = models.CharField(max_length=20)
    is_male = models.BooleanField(default=True,
                                  choices=((True, u'男'), (False, u'女')))
    birthday = models.DateTimeField(blank=True, null=True)
    mphone_num = models.CharField(max_length=11)
    mphone_short_num = models.CharField(max_length=6)
    student_id = models.CharField(max_length=10)
    szucard = models.CharField(max_length=6)
    login_count = models.IntegerField(default=0)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
