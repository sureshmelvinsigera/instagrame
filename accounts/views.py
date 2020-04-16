# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			#Log the user in
			login(request, user)
			return redirect('timeline:home')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/signup.html',{'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			## log in the user
			user = form.get_user()
			login(request, user)
			return redirect('timeline:home')
		signup_form = UserCreationForm(request.POST)
		if signup_form.is_valid():
			user = signup_form.save()
			#Log the user in
			login(request, user)
			return redirect('timeline:home')
	else:
		form = AuthenticationForm()
		signup_form = UserCreationForm()
	return render(request, 'accounts/login.html', {'form': form, 'signup_form':signup_form})

def logout_view(request):
	if request.method == 'GET':
		logout(request)
		return redirect('timeline:home')