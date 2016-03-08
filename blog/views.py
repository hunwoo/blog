from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from blog.models import Category, Comment
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.shortcuts import redirect
from blog.forms import PostEditForm
from blog.forms import CommentEditForm


def list_posts(request):
	page = request.GET.get('page',1)

	object_list = Post.objects.all().order_by('-created_at') # order_by()의 필드값 기준 따른 정렬, - 는 DESC!!
	per_page = 3 # 설정값에 따라 한 페이지에 보여주는 글 개수 변함.
	#object_list = Post.objects.filter(is_published = True)
	pn = Paginator(object_list, per_page)
	try:
		posts = pn.page(page)
	except PageNotAnInteger:
		posts = pn.page(1)
	except EmptyPage:
		posts = pn.page(pn.num_pages)
	ctx = {
		'posts' : posts,
	}
	return render(request, 'post_list.html', ctx)

def view_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comment_form = CommentEditForm()
	comments = Comment.objects.filter(post=post)

	#if the_post.is_published is True:
	return render(request, 'post_view.html',{
		'post' : post,
		'comment_form' : comment_form,
		'comments' : comments,
	})  #is_published가 True이면 해당 글 페이지로
	#else:
	#	return render(request, '404.html',ctx)# is_published가 False면 404페이지로

def category_posts(request, category_pk):
	object_list = Post.objects.filter(category__pk = category_pk).order_by('-created_at')
	page = request.GET.get('page',1)
	per_page = 2
	pn = Paginator(the_posts, per_page)
	try:
		posts = pn.page(page)
	except PageNotAnInteger:
		posts = pn.page(1)
	except EmptyPage:
		posts = pn.page(pn.num_pages)
	ctx = {
		'posts' : posts,
	}
	return render(request, 'post_list.html', ctx)

def create_post(request):
	if request.user.is_authenticated() is False:
		raise Exception('로그인을 해야합니다.')

	categories = Category.objects.all()

	if request.method == 'POST':
		form = PostEditForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('view_post', pk=post.pk)
	else:
		form = PostEditForm()
	return render(request, 'edit_post.html', {
		'categories': categories,
		'form' : form,
		})

def create_comment(request, pk):
	if request.user.is_authenticated() is False:
		raise Exception('로그인을 해야합니다.')

	post = get_object_or_404(Post, pk=pk)

	if request.method == 'POST':
		form = CommentEditForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.post = post
			comment.save()
			return redirect('view_post', pk=post.pk)
	else:
		form = CommentEditForm()
	return render(request, 'post_view.html',{
		'post' : post,
		'comment_form' : form,
		})

def remove_post(request,pk):
	if request.user.is_authenticated() is False:
		raise Exception('로그인을 해야 합니다.')
	# 여기에 글 작성자와 실제 삭제 요청자의 일치 여부를 확인하는 코드 필요함
	rm_post = Post.objects.get(pk=pk)
	rm_post.delete()
	return redirect('list_posts')

def remove_comment(request,pk):
	if request.user.is_authenticated() is False:
		raise Exception('로그인을 해야 합니다.')
	# 여기에 댓글 작성자와 실제 삭제 요청자의 일치 여부를 확인하는 코드 필요함
	rm_comment = Comment.objects.get(pk=pk)
	rm_comment.delete()
	return redirect('list_posts')


