from django.contrib import admin
from blog_app.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')
	list_filter = ('published', 'created')
	search_fields = ('title', 'description', 'content')
	date_hierarchy = 'created'
	save_on_top = True
	
#admin.site.register(Post)
admin.site.register(Post, PostAdmin)
