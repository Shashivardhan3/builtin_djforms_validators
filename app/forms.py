from typing import Any
from django import forms
from django.core import validators


def validation_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError("First letter should not be a")
def validation_for_length(value):
    if len(value)<=5:
        raise forms.ValidationError('length is less than 5')


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[validation_for_a,validation_for_length])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField(validators=[validation_for_a])
    Remail=forms.EmailField()
    mobile=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput)
    
    def clean(self):
        e=self.cleaned_data['Semail']
        r=self.cleaned_data['Remail']
        if e!=r:
            raise forms.ValidationError('email is not matched')
        
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            forms.ValidationError('bot')

