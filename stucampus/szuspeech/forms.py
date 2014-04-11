from django import forms

from stucampus.szuspeech.models import Resource


class ResourceForm(forms.ModelForm):
    resource_intro = forms.CharField(widget=forms.Textarea({'maxlength':200}))
    class Meta:
        model = Resource
        exclude = ('is_top')
