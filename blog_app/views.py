from django.shortcuts import render,get_object_or_404, HttpResponse
from blog_app.models import Post,Likes,details,comments
from . import models
try:
	from django.utils import simplejason as json
except ImportError:
	import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.text import slugify
from django.core import serializers

def testlogin(request):
	if request.user.is_authenticated():
		return 0
	else:
		return 1

def index(request):
	posts = Post.objects.filter(published=True)
	print request.user
	global notloggedin
	notloggedin = testlogin(request)
	return render(request, 'index.html', {'posts': posts, 'notloggedin':notloggedin, 'username': request.user})

def sort_opt(request):
	posts = Post.objects.all()
	data = [post.as_dict() for post in posts]
	return HttpResponse(json.dumps(data), content_type="application/json")

def post(request, slug):
	#print slug
	post = get_object_or_404(Post, slug=slug)
	notloggedin = testlogin(request)
	if notloggedin == 0:
		lk = Likes.objects.filter(posts=post, usr=request.user)
		if not lk:
			state = 'Like'
		else:
			state = 'Unlike'
	else:
		state = 'Like'
	return render(request, 'post.html', {'post':post, 'username': request.user, 'notloggedin':notloggedin, 'like':state, 'no_likes':post.no_likes})

def search(request):
	notloggedin = testlogin(request)
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		posts = Post.objects.filter(title__icontains=q)
		return render(request, 'search_results.html', {'posts': posts, 'query':q, 'username': request.user, 'notloggedin':notloggedin})
	else:
		return HttpResponse('Please submit a search term.')

def register_page(request):
	notloggedin = testlogin(request)
	return render(request, 'register.html' , {'notloggedin':notloggedin})

def register(request):
	notloggedin = testlogin(request)
	usr = request.GET.get('user')
	pss = request.GET.get('pass')
	eml = request.GET.get('email')
	posts = Post.objects.all()
	if(usr and pss and eml):
		User.objects.create_user(usr, eml, pss)
		return login_page(request)

def login_page(request):
	notloggedin = testlogin(request)
	return render(request, 'login_page.html', {'notloggedin':notloggedin})

def logins(request):
	usr = request.GET.get('user')
	pss = request.GET.get('pass')
	print usr, pss
	user = authenticate(username=usr,password=pss)
	if user is not None:
		if user.is_active:
			login(request, user)
			return index(request)
		else:
			print("password valid but account inactive")
	else:
		print("username and password incorrect")
		
def logouts(request):
	logout(request)
	return index(request)

def my_account_page(request):
	notloggedin = testlogin(request)
	uname = request.user.username
	fname = request.user.first_name
	lname = request.user.last_name
	email = request.user.email
	try:
		phno = request.user.details.ph_no
	except AttributeError:
		phno = 0
	return render(request, 'my_account.html', {'ph_no':phno, 'notloggedin':notloggedin, 'lname':lname,'email':email, 'fname':fname, 'uname':uname, 'notloggedin':notloggedin, 'username': request.user })

def change_info(request):
	uname = request.GET.get('uname')
	fname = request.GET.get('fname')
	lname = request.GET.get('lname')
	email = request.GET.get('email')
	phno = request.GET.get('ph_no')
	request.user.username = uname
	request.user.first_name = fname
	request.user.last_name = lname
	request.user.email = email
	request.user.details.ph_no = phno
	request.user.save()
	return index(request)

def liked(request):
	print "inlikes"
	cur_post = get_object_or_404(Post, slug=request.POST.get('slug'))
	if request.user.is_authenticated():
 		lk = Likes.objects.filter(posts=cur_post, usr=request.user)
 		#post1 = Post.objects.get(slug=cur_post.slug)
 		if not lk:
 			Likes.objects.create(posts=cur_post, usr=request.user)
 			no = cur_post.no_likes + 1;
 			cur_post.no_likes = no
 			cur_post.save()
 		else:
 			lk.delete()
 			no = cur_post.no_likes - 1
 			cur_post.no_likes = no
 			cur_post.save()
 		ctx = {"likes": no}
 		return HttpResponse(json.dumps(ctx), content_type="application/json")
 	else:
 		return login_page(request)

def post_form(request):
	notloggedin = testlogin(request)
	return render(request, 'post_form.html', {'username': request.user, 'notloggedin':notloggedin})

def send_request(request):
	titl = request.GET.get('title')
	cont = request.GET.get('content')
	desc = request.GET.get('descrip')
	slg =  slugify(titl)
	Post.objects.create(title=titl, content=cont, description=desc, slug=slg)
	return index(request)

def commenting(request):
	#import pdb; pdb.set_trace()
	if(request.method == 'GET'):
		cur_post = get_object_or_404(Post, slug=request.GET.get('slug'))
	if(request.method == 'POST'):
		cur_post = get_object_or_404(Post, slug=request.POST.get('slug'))
		comments.objects.create(comnt=request.POST.get('comment'), slug=cur_post.slug, user=request.user)
	coms = comments.objects.filter(slug=cur_post.slug)
	data = [com.as_dict() for com in coms]
	#actual_data = [d['fields'] for d in data]
	#data = serializers.serialize("json", coms)
	return HttpResponse(json.dumps(data), content_type="application/json")

