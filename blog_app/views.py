from django.shortcuts import render,get_object_or_404
from blog_app.models import Post,Likes
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

notloggedin = 1
cur_post=[]

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
	lk = Likes.objects.filter(posts=post, usr=request.user)
	if not lk:
		state = 'Like'
	else:
		state = 'Unlike'
	global cur_post
	cur_post=post
	return render(request, 'post.html', {'post':post, 'username': request.user, 'notloggedin':notloggedin, 'like':state})

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
	global notloggedin
	user = authenticate(username=usr,password=pss)
	if user is not None:
		if user.is_active:
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

def my_account_page(request):
	if request.user.is_authenticated():
		notloggedin = 0
	else:
		notloggedin = 1
	uname = request.user.username
	fname = request.user.first_name
	lname = request.user.last_name
	email = request.user.email
	request.user.save()
	return render(request, 'my_account.html', {'notloggedin':notloggedin, 'lname':lname,'email':email, 'fname':fname, 'uname':uname, 'notloggedin':notloggedin, 'username': request.user })

def change_info(request):
	uname = request.GET.get('uname')
	fname = request.GET.get('fname')
	lname = request.GET.get('lname')
	email = request.GET.get('email')
	request.user.username = uname
	request.user.first_name = fname
	request.user.last_name = lname
	request.user.email = email
	return index(request)

def liked(request):
	cur_post
 	lk = Likes.objects.filter(posts=cur_post, usr=request.user)
 	no = cur_post.no_likes;
 	no += 1
 	print cur_post.slug, no, lk
 	post1 = Post.objects.get(slug=cur_post.slug)
 	print post1
 	if not lk:
 		Likes.objects.create(posts=post1, usr=request.user)
 		print "in if"
 		post1.no_likes = no
 		post1.save()
 	else:
 		unlike(request)
 	print lk
 	return post(request, cur_post.slug)

def unlike(request):
	lk = Likes.objects.filter(posts=cur_post, usr=request.user)
	lk.delete()
	no = cur_post.no_likes - 1
	cur_post.no_likes = no
	cur_post.save()
	return post(request, cur_post.slug)
