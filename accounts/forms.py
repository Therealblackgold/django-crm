from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import Member


class MemberCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = Member
        fields = [
            'username', 'first_name', 'last_name', 'phone_number',
            'phone_number_2', 'id_number', 'address', 'package', 'email',
            'password1', 'password2'
        ]

        widgets = {
            'package':
            forms.SelectMultiple(attrs={
                'class': 'form-select',
            }),
            'username':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'first_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@thuso.com'
            }),
            'password1':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
            'password2':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
            'phone_number':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'id_number_2':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Number'
            }),
            'address':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'address'
            }),
        }


class MemberCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Member
        fields = [
            'username', 'first_name', 'last_name', 'id_number', 'email',
            'phone_number', 'phone_number_2', 'package', 'address',
            'password1', 'password2'
        ]

        # widgets = {
        #     'package':
        #     forms.SelectMultiple(attrs={
        #         'class': '',
        #         'style': 'background-color: grey;'
        #     }),
        # }
