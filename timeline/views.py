# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Post
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required(login_url="/accounts/login")
def timeline(request):
	posts = Post.objects.all().order_by('-date')
	for post in posts:
		post.is_liked = (request.user in post.likes.all())
		post.defpic = Profile.objects.get(user_name_id=post.author_id)
	return render(request, 'timeline/index.html', {'posts':posts})

@login_required(login_url="/accounts/login")
def share(request):
	if request.method == 'POST':
		form = forms.SharePost(request.POST, request.FILES)
		if form.is_valid():
			#save post to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('timeline:home')
	else:
		form = forms.SharePost()
	return render(request, 'timeline/share.html', {'form': form})
