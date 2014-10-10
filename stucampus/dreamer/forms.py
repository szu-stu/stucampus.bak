from django import forms

from stucampus.dreamer.models import Application


class AppForm(forms.ModelForm):

    self_intro = forms.CharField(widget=forms.Textarea({'maxlength': 200}))

    class Meta:
        model = Application
        exclude = ('apply_date')
