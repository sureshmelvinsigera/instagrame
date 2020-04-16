# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from timeline.models import Post
from accounts.models import Profile
from . import forms

# Create your views here.

@login_required(login_url="/accounts/login")
def profile_view(request):
	posts = Post.objects.filter(author=request.user)
	profile = Profile.objects.get(user_name=request.user)
	return render(request, 'profile_page/index.html', {'posts':posts, 'profile':profile})

def author_profile_view(request, author):
	posts = Post.objects.filter(author__username=author)
	author_username = posts[0].author
	return render(request, 'profile_page/index.html', {'posts':posts, 'author_username':author_username})

def post_details(request, id):
	image = Post.objects.get(id=id)
	image.is_liked = (request.user in image.likes.all())
	return render(request, 'profile_page/image-details.html', {'image':image})

@login_required(login_url="/accounts/login")
def edit_profile(request):
	if request.method == 'POST':
		form = forms.Profile(request.POST, request.FILES)
		if form.is_valid():
			#save post to db
			instances = form.save(commit=False)
			instances.user_name = request.user
			instances.save()
			return redirect('profiles:index')
	else:
		form = forms.Profile()
	return render(request, 'profile_page/edit.html', {'form': form})

class PostLikeToggle(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		id = self.kwargs.get("id")
		print(id)
		obj = get_object_or_404(Post, id=id)
		url_ = obj.get_absolute_url()
		user = self.request.user
		if user.is_authenticated:
			is_liked=False
			if user in obj.likes.all():
				obj.likes.remove(user)
				is_liked= False
			else:
				obj.likes.add(user)
				is_liked= True
		return url_

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class PostLikeAPIToggle(APIView):
	authentication_classes = [authentication.SessionAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, id=None, format=None):
		id = self.kwargs.get("id")
		obj = get_object_or_404(Post, id=id)
		url_ = obj.get_absolute_url()
		user = self.request.user
		updated = False
		liked = False
		if user.is_authenticated:
			if user in obj.likes.all():
				obj.likes.remove(user)
				liked = False
			else:
				obj.likes.add(user)
				liked = True
			updated = True
		data = {
			'updated': updated,
			'liked': liked,
		}
		return Response(data)