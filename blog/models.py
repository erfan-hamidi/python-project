from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField()