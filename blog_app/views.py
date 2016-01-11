from django.shortcuts import render,get_object_or_404
from blog_app.models import Post,Users
from . import models

reg = 1
logged = 1

def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts': posts, 'reg':reg, 'login':logged})

def post(request, slug):
	#print slug
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'post.html', {'post':post})

def search(request):

	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		posts = Post.objects.filter(title__icontains=q)
		return render(request, 'search_results.html', {'posts': posts, 'query':q})
	else:
		return HttpResponse('Please submit a search term.')
def register_page(request):
	return render(request, 'register.html')

def register(request):
	usr = request.GET.get('user')
	pss = request.GET.get('pass')
	eml = request.GET.get('email')
	reg = 0
	posts = Post.objects.all()
	logged = 0
	if(usr and pss and eml):
		Users.objects.create(username=usr, password=pss, email=eml)
		return render(request, 'index.html', {'username':usr, 'posts': posts, 'reg':reg, 'login':logged})
def login_page(request):
	return render(request, 'login_page.html')

def login(request):
	usr = request.GET.get('user')
	pss = request.GET.get('pass')
	logged=0
	reg=0
	posts = Post.objects.all()
	if usr and pss:
		rec = Users.objects.get(username=usr)
		if rec.password == pss:
			return render(request, 'index.html', {'username':usr, 'posts': posts, 'reg':reg, 'login':logged})

def logout(request):
	logged=1
	reg=1
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts': posts, 'reg':reg, 'login':logged})
