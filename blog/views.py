from datetime import date
from django.db.models.query import QuerySet

from django.shortcuts import render , get_object_or_404

from blog.models import Post
from django.views.generic import ListView

all_posts = [
    
]

def get_date(post):
  return post['date']

# Create your views here.


class StartingPage(ListView):
  template_name = "blog/index.html"
  modol = Post
  ordering = ["-date"]
  
  def get_queryset(self):
      queryset = super().get_queryset()
      date = queryset[:3]
      return date



def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug = slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post,
      "post_tags": identified_post.tag.all()
    })
