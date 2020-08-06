import django_filters
from django_filters import CharFilter
from .models import Subject
from django import forms



class sub_filter(django_filters.FilterSet):
    name = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='name', lookup_expr='icontains', label='name')
    code = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='code', lookup_expr='icontains', label='code')
    credit = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='credit', lookup_expr='icontains', label='credit')
    class Meta:
        model = Subject
        fields = ['name', 'code', 'credit']