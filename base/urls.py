from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('posts/', views.posts, name = 'posts'),
	path('post/<pk>', views.post, name = 'post'),
	path('profile/', views.profile, name = 'profile'),
	path('sendEmail/', views.sendEmail, name = 'send_email')
	
]