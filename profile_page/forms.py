from django import forms
from accounts import models

class Profile(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['def_picture','biography']