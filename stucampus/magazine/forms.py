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

    def clean(self):
        if 'issue' not in self.cleaned_data or \
           'name' not in self.cleaned_data:
            return super(MagazineForm, self).clean()
        if Magazine.objects.filter(
                name=self.cleaned_data['name'],
                issue=self.cleaned_data['issue']
                ).exclude( pdf_file=self.cleaned_data['pdf_file']).exists():
            msg = u'该期数已存在'
            self._errors['issue'] = self.error_class([msg])
            del self.cleaned_data['issue']
        return self.cleaned_data

