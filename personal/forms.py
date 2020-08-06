from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from .models import *
from django.shortcuts import render


class subject_form(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name', 'code', 'credit']


class ans_form(forms.ModelForm):
    name_subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = credit_reg
        fields = ['student', 'name_subjects']

