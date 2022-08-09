from turtle import textinput
from django import forms
from .models import User
from django.core import validators


class StudenResgitration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','company']
        labels = {'pasword': ['Company']}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'company': forms.TextInput(attrs={'class':'form-control'})}
        