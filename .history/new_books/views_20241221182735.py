from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from .models import Author
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin


class HomeView(TemplateView):
    template_name = 'new_books/home.html'
    
    
class AuthorView(ListView):
    model = Author
    template_name = 'new_books/author_list.html'
    context_object_name = 'authors'
 
 
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'new_books/author_detail.html'
    context_object_name = 'auth'
    
        
class AuthorCreateview(CreateView):
    model = Author
    template_name = 'new_books/author_create.html'
    fields = ['name',]
    
    
    def form_valid(self, form):
        
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Author has been created'
        )
        
        return super().form_valid(form)

class AuthorBooksEdit(SingleObjectMixin, FormView):
    
    model = Author
    template_name = 'new_books/author_books_edit.html'
    
    def get(self, request, *args, **kwargs):
        self