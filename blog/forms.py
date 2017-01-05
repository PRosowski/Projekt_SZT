from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
