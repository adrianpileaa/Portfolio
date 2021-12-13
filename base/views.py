from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def home(request):
	context = {}
	posts = Post.objects.all()
	context['posts'] = posts
	return render(request, 'base/index.html',context)


def posts(request):
	context = {}
	posts = Post.objects.all()
	context['posts'] = posts
	return render(request, 'base/posts.html',context)

def post(request, pk):
	context = {}
	post = Post.objects.get(id = pk)
	context['post'] = post
	return render(request, 'base/post.html', context)

def profile(request):
	return render(request, 'base/profile.html')
def sendEmail(request):

	if request.method == 'POST':
		template = render_to_string('base/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['adrianpilea51@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'base/email_sent.html')