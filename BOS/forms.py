from django import forms
from .models import adypu_data

class editform(forms.ModelForm):
    class Meta:
        model = adypu_data
        fields = '__all__'