from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length = 255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	no_likes = models.IntegerField(default=0)
	published = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		print self.slug
		return reverse('blog_app.views.post', kwargs={'slug':self.slug,})

class Likes(models.Model):
	posts = models.ForeignKey(Post)
	usr = models.ForeignKey(User)

class comments(models.Model):
	user = models.TextField()
	comnt = models.TextField()
	slug = models.CharField(default="", max_length = 255)

	def as_dict(self):
		return {
			"user": self.user,
			"comnt": self.comnt,
			"slug": self.slug,
        }

class details(models.Model):
	user = models.OneToOneField(User)
	ph_no = models.IntegerField(default=0)

class Meta:
    ordering = ['-created']
    def __unicode__(self):
    	return u'%s' % self.title