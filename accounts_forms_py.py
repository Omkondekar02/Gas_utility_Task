# -*- coding: utf-8 -*-
"""accounts/forms.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14rl4p8_tdbM5_mfF6q9KdZ1bRaTKlj-C
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomerProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    address = forms.CharField(max_length=255, required=True, help_text='Required. Enter your complete address.')
    phone_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter your phone number.')
    account_number = forms.CharField(max_length=20, required=True, help_text='Required. Enter your gas utility account number.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CustomerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ('address', 'phone_number')