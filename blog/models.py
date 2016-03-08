from django.db import models
from django.conf import settings


class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=200)
	content = models.TextField()
	category = models.ForeignKey('Category')
	is_published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return '{pk}: {category} - {title}'.format(
			pk = self.pk,
			title = self.title,
			category = self.category,
			)

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.ForeignKey(Post)
	comment = models.TextField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Post {post_pk}: Comment {pk}'.format(
			post_pk=self.post.title,
			pk=self.pk,
			)

class Category(models.Model):
	name = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name








# Create your models here.
