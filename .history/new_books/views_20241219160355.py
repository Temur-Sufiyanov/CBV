from django.shortcuts import render
from django.views.generic import (TemplateView, ListView)
# Create your views here.

class HomeView(TemplateView):
    template_name = 'new_books/home.html'
    
class Author
