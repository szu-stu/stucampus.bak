#-*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from stucampus.minivideo.models import Resource

class SignUpForm(forms.ModelForm):
    team_captain = forms.CharField(
        label=_(u'队长姓名'),max_length=12,
        error_messages={'required': _(u'此字段必填')}
    )
    Team_captain_phone = forms.CharField(
        label=_(u'队长电话'),max_length=11,
        error_messages={'required': _(u'此字段必填')}
    )
    Team_captain_stuno = forms.CharField(
        label=_(u'队长学号'),max_length=10,
        error_messages={'required': _(u'此字段必填')}
    )
    Team_captain_college = forms.CharField(
        label=_(u'队长学院'),max_length=None,
        error_messages={'required': _(u'此字段必填')}
    )
    team_members1_name = forms.CharField(
        label=_(u'队员一姓名'),max_length=12, required=False,
    )
    team_members1_id = forms.CharField(
        label=_(u'队员一学号'),max_length=10, required=False,
    )
    team_members2_name = forms.CharField(
        label=_(u'队员二姓名'),max_length=12, required=False,
    )
    team_members2_id = forms.CharField(
        label=_(u'队员二学号'),max_length=10, required=False,
    )
    team_members3_name = forms.CharField(
        label=_(u'队员三姓名'),max_length=12, required=False,
    )
    team_members3_id = forms.CharField(
        label=_(u'队员三学号'),max_length=10, required=False,
    )
    team_members4_name = forms.CharField(
        label=_(u'队员四姓名'),max_length=12, required=False,
    )
    team_members4_id = forms.CharField(
        label=_(u'队员四学号'),max_length=10, required=False,
    )
    team_members5_name = forms.CharField(
        label=_(u'队员五姓名'),max_length=12, required=False,
    )
    team_members5_id = forms.CharField(
        label=_(u'队员五学号'),max_length=10, required=False,
    )
    team_psw = forms.CharField(
        label=_(u'team_psw'), max_length=30,
        widget=forms.PasswordInput(),
        error_messages={
            'required': _(u'此字段必填'),
            'max_length': _(u'密码长度不得超过30')
        }
    )
    confirm = forms.CharField(
        label=_(u'密码确认'), max_length=30,
        widget=forms.PasswordInput(),
        error_messages={
            'required': _(u'此字段必填'),
            'max_length': _(u'密码长度不得超过30')
        }
    )

    def clean_confirm(self):
        team_psw = self.cleaned_data.get('team_psw')
        confirm = self.cleaned_data.get('confirm')
        if not team_psw == confirm:
            raise forms.ValidationError(_(u'前后输入密码不一致'))
        return confirm

    class Meta:
         model = Resource
         exclude = ('video_cover', 'video_name', 'video_intro', 'video_link', 'votes', 'has_verified')
        