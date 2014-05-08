#-*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from stucampus.minivideo.models import Resource

class SignUpForm(forms.ModelForm):
    
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
        
