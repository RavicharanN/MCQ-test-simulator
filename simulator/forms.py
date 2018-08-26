from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(label='password',widget= forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']