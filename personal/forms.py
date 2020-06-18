from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from .models import *


class subject_form(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name', 'credit']