# -*- coding: utf-8 -*-
"""accounts/views.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14rl4p8_tdbM5_mfF6q9KdZ1bRaTKlj-C
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileUpdateForm, CustomerProfileUpdateForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.customerprofile.account_number = form.cleaned_data.get('account_number')
            user.customerprofile.address = form.cleaned_data.get('address')
            user.customerprofile.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            messages.success(request, 'Your account has been created! You can now login.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        profile_form = CustomerProfileUpdateForm(request.POST, instance=request.user.customerprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = ProfileUpdateForm(instance=request.user)
        profile_form = CustomerProfileUpdateForm(instance=request.user.customerprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/update_profile.html', context)