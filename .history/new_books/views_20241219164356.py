from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView)
from .models import Author
from django.contrib import messages
# Create your views here.

class HomeView(TemplateView):
    template_name = 'new_books/home.html'
    
    
class AuthorView(ListView):
    model = Author
    template_name = 'new_books/author_list.html'
    context_object_name = 'authors'
    
class AuthorCreateview(CreateView):
    model = Author
    template_name = 'new_books/author_create.html'
    fields = ['name',]
    
    
    def form_valid(self, form):
        
        messages.add_message(
            self.request,
            me
        )
