from django import forms
from . import models

class SharePost(forms.ModelForm):
	class Meta:
		model = models.Post
		fields = ['title','location','caption','photo']