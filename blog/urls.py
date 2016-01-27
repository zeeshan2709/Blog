"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from blog_app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', views.search),
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register),
    url(r'^login_page/$', views.login_page, name='logpage'),
    url(r'^logins/$', views.logins),   
    url(r'^logouts/$', views.logouts, name='logouts'),
    url(r'^myaccount/$', views.my_account_page, name='acc_page'),
    url(r'^change_info/$', views.change_info),
    url(r'^liked/$', views.liked, name='liked'),
    url(r'^comment/$', views.commenting, name='comment'),
    url(r'^sort_op/$', views.sort_opt, name='sort'),
    url(r'^post_form/$', views.post_form, name='post_form'),
    url(r'^send_request/$', views.send_request),
    url(r'^register_page/$', views.register_page, name='regpage'),
    url(r'^(?P<slug>[\w\-]+)/$', views.post),
]
