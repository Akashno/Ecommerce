from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput


class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mt-3', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mt-3', 'placeholder':'Confirm Password'}),
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username':TextInput(attrs={
                'required':'true',
                'class':'form-control mt-3',
                'name':'username',
                'id':'username',
                'placeholder':'Username',
            }),
            'first_name': TextInput(attrs={
                'required':'true',
                'class': 'form-control mt-3',
                'name': 'first_name',
                'id': 'first_name',
                'placeholder': 'First Name',
            }),
            'last_name': TextInput(attrs={
                'required':'true',
                'class': 'form-control mt-3',
                'name': 'last_name',
                'id': 'last_name',
                'placeholder': 'Last Name',
            }),
            'email': TextInput(attrs={
                'required':'true',
                'class': 'form-control mt-3',
                'name': 'email',
                'id': 'email',
                'placeholder': 'Email',
            }),

        }