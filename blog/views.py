from datetime import date
from django.db.models.query import QuerySet

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
  template_name = "blog/post-detail.html"
  model = Post

  def get(self, req, slug):
    post = Post.objects.get(slug=slug)
    context = {
      "post": post,
      "posts_tags" : Post.tag.all(),
      "comment_form": CommentForm()
    }
    return render(req, "blog/post-detail.html", context)

  def post(self, req):


  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["posts_tags"] = self.object.tag.all()
      context["comment_form"] = CommentForm()
      return context
