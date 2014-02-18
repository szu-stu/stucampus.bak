#-*- coding: utf-8
from django import forms
from django.forms.models import modelformset_factory

from stucampus.magazine.models import Magazine


class MagazineForm(forms.ModelForm):
    NAME_CHOICE = (
            (u'深大青年', u'深大青年'),
            (u'浪淘沙', u'浪淘沙'),
            )
    name = forms.ChoiceField(choices=NAME_CHOICE)
    class Meta:
        model = Magazine

