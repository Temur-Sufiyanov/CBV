from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    name = models.CharField(null=False, blank=False, max)
