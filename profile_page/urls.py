from django.conf.urls import url
from . import views

app_name='profiles'

urlpatterns = [
	url(r'^$', views.profile_view, name="index"),
	url(r'^edit/$', views.edit_profile, name='edit_profile'),
	url(r'^(?P<id>\d+)/$', views.post_details, name="post-details"),
	url(r'^(?P<id>\d+)/like/$', views.PostLikeToggle.as_view(), name="like-toggle"),
	url(r'^api/(?P<id>\d+)/like/$', views.PostLikeAPIToggle.as_view(), name="like-api-toggle"),
	url(r'^(?P<author>[\w-]+)/$', views.author_profile_view, name="author-profile"),
]