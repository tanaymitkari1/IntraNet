from django import forms
from .models import Choice, Placements, Answer

class choice_form(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['placement', 'text']

class ans_form(forms.ModelForm):
    username = forms.CharField(help_text='Confirm your URN here')
    class Meta:
        model = Answer
        fields = ['placement', 'user', 'username', 'firstname', 'lastname']