from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog_app.models import Post,Likes
from blog_app.models import details
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')
	list_filter = ('published', 'created')
	search_fields = ('title', 'description', 'content')
	date_hierarchy = 'created'
	save_on_top = True
	
class detailsInline(admin.StackedInline):
	model = details
	can_delete = False
	verrbose_name_plural = 'details'

class UserAdmin(UserAdmin):
	inlines = (detailsInline, )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
#admin.site.register(Post)
admin.site.register(Post, PostAdmin)
admin.site.register(Likes)
