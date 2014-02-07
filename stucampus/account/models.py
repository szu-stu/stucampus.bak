#-*- coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    class Meta:
        permissions = (
            ('students_list', u'列出所有学生帐号List all students'),
            ('student_show', u'展示学生帐号信息Show the information of student.'),
            ('student_create', u'创建学生帐号Create a new student.'),
            ('student_edit', u'修改学生信息Edit the information of students.'),
            ('student_del', u'删除学生帐号Delete students'),

            ('org_managers_list', u'列出所有组织管理员List all managers of an organization.'),
            ('org_managers_create', u'创建新管理员Create a new manager.'),
            ('org_managers_del', u'删除组织管理员Remove a manager from an organization.'),
            ('members_list', u'列出组织所有成员List the members in an organization.'),
            ('member_show', u'展示成员信息Show the information of member.'),
            ('member_create', u'创建新组织成员Create a new member in organization.'),
            ('member_del', u'删除组织成员Remove a member from an organization.')
        )

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
    gender = models.CharField(default="M", max_length=1,
                              choices=(("M", u'男'), ("F", u'女')))
    birthday = models.DateTimeField(blank=True, null=True)
    mobile_phone_number = models.CharField(max_length=11)
    internal_phone_number = models.CharField(max_length=6)
    job_id = models.CharField(max_length=10)
    card_id = models.CharField(max_length=6)


class UserActivityLog(models.Model):
    user = models.ForeignKey(User)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    behavior = models.CharField(max_length=250)
