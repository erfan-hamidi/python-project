from django.contrib import admin

# Register your models here.
from blog.models import Author, Tag, Post

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)