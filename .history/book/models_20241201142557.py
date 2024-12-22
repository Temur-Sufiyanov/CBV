from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    slug = models.SlugField(null=True)
    count = models.IntegerField(null=True, default=0)