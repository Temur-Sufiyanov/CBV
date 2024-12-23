from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)#
    
    def get_absolute_url(self):
        return reverse('books:author_detail', kwargs={'pk': self.pk})
    
    def get_absolute_url(self):
        return reverse('books:add-author', )
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    author = models.ForeignKey('Author', null=False, blank=False, on_delete=models.CASCADE, related_name='book_author')
    
    
    def __str__(self):
        return self.name
