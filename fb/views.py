# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def timeline(request):
	return render(request, 'fb/index.html')