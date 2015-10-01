from django import forms

from stucampus.dreamer.models import DEPT


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=6)
    stu_ID = forms.IntegerField(max_value=2015159999, min_value=2010000000)
    college = forms.CharField(max_length=30)
    mobile = forms.CharField(max_length=11)
    dept1 = forms.CharField(choices=DEPT)
    dept2 = forms.CharField(choices=DEPT)
    self_intro = forms.CharField(widget=forms.Textarea({'max_length': 500}))
