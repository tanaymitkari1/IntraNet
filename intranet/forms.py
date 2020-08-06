from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group
from placement.models import *



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, help_text='')
    username = forms.CharField(help_text='add your URN')
    roles = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password']

        lable = {
            'password': 'Password'
        }


    def __init__(self, *args, **kwargs):
        if kwargs.get('instancs'):
            initial = kwargs.setdefault('initial', {})
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None

        forms.ModelForm.__init__(self, *args, **kwargs)



    def clean_email(self):
        if self.cleaned_data['email'].endswith('@adypu.edu.in'):
            return self.cleaned_data['email']
        else:
            raise ValidationError("use university email")
        
    def save(self):
        password = self.cleaned_data.pop('password')
        role = self.cleaned_data.pop('roles')
        u = super().save()
        u.groups.set([role])
        u.set_password(password)
        u.save()
        return u
