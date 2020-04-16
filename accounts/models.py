# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
	def_picture = models.ImageField(default='default.jpg', blank=True)
	biography = models.TextField(max_length=100, blank=True)
	user_name = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING,)

	def __str__(self):
		return self.user_name.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user_name=kwargs['instance'])

post_save.connect(create_profile, sender=User)