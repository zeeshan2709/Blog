from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length = 255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		print self.slug
		return reverse('blog_app.views.post', kwargs={'slug':self.slug,})

class Users(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
     
class Meta:
    ordering = ['-created']
    def __unicode__(self):
    	return u'%s' % self.title