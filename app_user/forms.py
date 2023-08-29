from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField( max_length=30, required=True)

