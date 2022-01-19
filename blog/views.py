from datetime import date
from re import I
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render , get_object_or_404
from .forms import CommentForm

from blog.models import Post, Tag
from django.views.generic import ListView , DetailView
from django.views import View
all_posts = [
    
]

def get_date(post):
  return post['date']

# Create your views here.


class StartingPage(ListView):
  template_name = "blog/index.html"
  model = Post
  ordering = ["-date"]
  context_object_name = "posts"
  
  def get_queryset(self):
      queryset = super().get_queryset()
      date = queryset[:3]
      return date

class Posts(ListView):
  template_name = "blog/all-posts.html"
  model = Post
  ordering = ["-date"]
  context_object_name = "all_posts"

class PostDetail(View):

  def get(self, req, slug):
    post = Post.objects.get(slug=slug)
    context = {
      "post": post,
      "posts_tags" : post.tag.all(),
      "comment_form": CommentForm(),
      "comments": post.comments.all().order_by("-id")
    }
    return render(req, "blog/post-detail.html", context)

  def post(self, req, slug):
    comment_form = CommentForm(req.POST)
    post = Post.objects.get(slug=slug)

    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.save()
      return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

    context = {
      "post": post,
      "posts_tags" : post.tag.all(),
      "comment_form": CommentForm,
      "comments": post.comments.all().order_by("-id"),
    }
    return render(req, "blog/post-detail.html", context)

