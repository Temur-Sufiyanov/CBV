from django.db import models
import slugi
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=59)
    slug = models.SlugField(null=True)
    count = models.IntegerField(null=True, default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = sluf
    def __str__(self):
        return self.title