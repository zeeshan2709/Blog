from django.shortcuts import render,get_object_or_404
from blog_app.models import Post,Users
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
user_n=""
notloggedin = 1
def index(request):
	posts = Post.objects.all()
	print request.user
	notloggedin = 1
	if request.user.is_authenticated():
		notloggedin = 0
	else:
		notloggedin = 1
	return render(request, 'index.html', {'posts': posts, 'notloggedin':notloggedin, 'username': request.user})

def post(request, slug):
	#print slug
	if request.user.is_authenticated():
		notloggedin = 0
	else:
		notloggedin = 1
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'post.html', {'post':post, 'username': request.user, 'notloggedin':notloggedin})

def search(request):

	if request.user.is_authenticated():
		notloggedin = 0
	else:
		notloggedin = 1
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		posts = Post.objects.filter(title__icontains=q)
		return render(request, 'search_results.html', {'posts': posts, 'query':q, 'username': request.user, 'notloggedin':notloggedin})
	else:
		return HttpResponse('Please submit a search term.')
def register_page(request):
	return render(request, 'register.html' , {'notloggedin':notloggedin})

def register(request):
	usr = request.GET.get('user')
	pss = request.GET.get('pass')
	eml = request.GET.get('email')
	posts = Post.objects.all()
	if(usr and pss and eml):
		User.objects.create_user(usr, eml, pss)
		return render(request, 'login_page.html')
def login_page(request):
	return render(request, 'login_page.html', {'notloggedin':notloggedin})

def logins(request):
	usr = request.GET.get('user')
	pss = request.GET.get('pass')
	print usr, pss
	user = authenticate(username=usr,password=pss)
	if user is not None:
		if user.is_active:
			user_n=usr
			notloggedin = 0
			login(request, user)
			return index(request)
		else:
			print("password valid but account inactive")
	else:
		print("username and password incorrect")
def logouts(request):
	logout(request)
	notloggedin = 1
	return index(request)
