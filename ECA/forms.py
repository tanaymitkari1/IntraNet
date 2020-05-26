from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User

class workshop_add(ModelForm):
    title = forms.CharField(label='Title',widget=forms.TextInput(attrs={'class': 'form-control'}))
    information = forms.CharField(label='Information', widget=forms.TextInput(attrs={'class': 'form-control'}))
    created_by = forms.ModelChoiceField(label='Created by', queryset=User.objects.all(), widget=forms.Select(attrs={'class': "form-control"}))
    start_date = forms.CharField(label='Start Date', widget=forms.TextInput(attrs={'class': "form-control"}))
    end_date = forms.CharField(label='End Date', widget=forms.TextInput(attrs={'class': "form-control"}))
    status = forms.CharField(label='Status', widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = add_eca
        fields = ['title', 'information', 'created_by', 'start_date', 'end_date', 'status']