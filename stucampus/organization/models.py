#-*- coding: utf-8
from django.db import models

from stucampus.account.models import Student


class Organization(models.Model):

    class Meta:
        permissions = (
            ('organizations_list', u'列出所有组织List all organizations'),
            ('organization_show', u'展示组织信息Show information of an organization.'),
            ('organization_create', u'创建新组织Create an organization'),
            ('organization_edit', u'修改组织信息Edit information of an organization'),
            ('organization_del', u'删除组织Delete an organization')
        )

    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    url = models.URLField()
    logo = models.CharField(max_length=50)
    managers = models.ManyToManyField(Student, related_name='orgs_as_manager')
    members = models.ManyToManyField(Student, related_name='orgs_as_member')
    is_banned = models.BooleanField(default=False)
    ban_reason = models.CharField(max_length=250, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
