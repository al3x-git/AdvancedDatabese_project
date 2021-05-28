from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2', )


class SocialIssueForm(ModelForm):

    class Meta:
        model = SocialIssue
        fields = '__all__'
