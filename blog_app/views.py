from django.shortcuts import render,get_object_or_404
from blog_app.models import Post
from . import models

def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts': posts})

def post(request, slug):
	print slug
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'post.html', {'post':post})

def search(request):

	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		posts = Post.objects.filter(title__icontains=q)
		return render(request, 'search_results.html', {'posts': posts, 'query':q})
	else:
		return HttpResponse('Please submit a search term.')
