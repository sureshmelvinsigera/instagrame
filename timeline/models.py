# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from facebuuk.utils import unique_slug_generator

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug  = models.SlugField(null=True, blank=True)
	location = models.CharField(max_length=100, null=True)
	caption = models.TextField(max_length=200)
	likes = models.ManyToManyField(User, blank=True, related_name='likes')
	date = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField()
	author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.caption[:50]+'...'

	def get_absolute_url(self):
		return reverse("profiles:post-details", kwargs={"id":self.id})
	
	def get_like_url(self):
		return reverse("profiles:like-toggle", kwargs={"id": self.id})

	def get_api_like_url(self):
		return reverse("profiles:like-api-toggle", kwargs={"id": self.id})

def slug_generator(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)

