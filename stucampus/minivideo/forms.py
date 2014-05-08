#-*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from stucampus.minivideo.models import Resource

class SignUpForm(forms.ModelForm):

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
        team_psw =  self.objects.get('team_psw')
        confirm = self.cleaned_data.get('confirm')
        if not team_psw == confirm:
            raise forms.ValidationError(_(u'前后输入密码不一致'))
        return confirm

    class Meta:
         model = Resource
         exclude = ('video_cover', 'video_name', 'video_intro', 'video_link', 'votes', 'has_verified')

class CommitForm(forms.ModelForm):

    confirm = forms.CharField(
        label=_(u'密码'), max_length=30,
        widget=forms.PasswordInput(),
        error_messages={
            'required': _(u'此字段必填'),
            'max_length': _(u'密码长度不得超过30')
        }
    )

    def clean_confirm(self):
        team_psw = Resource.objects.get('team_psw')
        confirm = self.cleaned_data.get('confirm')
        if not team_psw == confirm:
            raise forms.ValidationError(_(u'密码错误'))
        return confirm

    class Meta:
         model = Resource
         exclude = ('team_captain', 'team_captain_phone', 
            'team_captain_stuno', 'team_captain_college',
            'team_members1_name', 'team_members1_id',
            'team_members2_name', 'team_members2_id',
            'team_members3_name', 'team_members3_id', 
            'team_members4_name', 'team_members4_id', 
            'team_members5_name', 'team_members5_id',
            'team_psw', 'votes', 'has_verified')


        
