import django_filters
from django_filters import DateFilter, CharFilter
from .models import adypu_data
from django import forms

class adypu_filter(django_filters.FilterSet):
    subject_name = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='subject_name', lookup_expr='icontains', label='Subject name')
    subject_code = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='subject_code', lookup_expr='icontains', label='Subject code')
    course_type = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='course_type', lookup_expr='icontains', label='Course Type')
    year_of_coding = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='year_of_coding', lookup_expr='icontains', label='Year of Coding')
    school_name = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='school_name', lookup_expr='icontains', label='School Name')
    specialization = CharFilter(widget=forms.TextInput(attrs={'class': 'col form-control'}),field_name='specialization', lookup_expr='icontains', label='Specialization')

    class Meta:
        model = adypu_data
        fields = ['subject_name', 'subject_code', 'course_type', 'year_of_coding', 'school_name', 'specialization']