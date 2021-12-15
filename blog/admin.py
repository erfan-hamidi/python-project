from django.contrib import admin

# Register your models here.
from blog.models import Author, Tag, Post

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date" , "tag")
    list_display = ("title", "date" , "author")
    prepopulated_fields = {"slug" : ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)