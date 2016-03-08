"""tumblog URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import list_posts
from blog.views import view_post
from blog.views import create_post
from blog.views import category_posts
from blog.views import create_comment
from blog.views import remove_post
from blog.views import remove_comment


urlpatterns = [
	url(r'^blog/posts/edit/$', create_post, name = 'create_post'),
	url(r'^blog/category/(?P<category_pk>[0-9]+)/$', category_posts, name='category_view_posts'),
	url(r'^blog/posts/(?P<pk>[0-9]+)/$', view_post, name='view_post'),
	url(r'^blog/(?P<pk>[0-9]+)/comment/$', create_comment, name = 'create_comment'),
	url(r'^blog/$', list_posts, name='list_posts'),
	url(r'^blog/posts/(?P<pk>[0-9]+)/remove_post/$', remove_post, name='remove_post'),
	url(r'^blog/posts/(?P<pk>[0-9]+)/remove_comment/$', remove_comment, name='remove_comment'),
    url(r'^admin/', admin.site.urls),    
]
