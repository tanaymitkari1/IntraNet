import django_filters
from .models import Answer
from django import forms

class answers_filter(django_filters.FilterSet):

    class Meta:
        model = Answer
        fields = ['username', 'firstname', 'lastname']