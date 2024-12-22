from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from .models import Author
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from .forms import AuthorBooksFormset


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

# class AuthorBooksEdit(SingleObjectMixin, FormView):
    
#     model = Author
#     template_name = 'new_books/author_books_edit.html'
    
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Author.objects.all())
#         return super().get(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         print("POST data:", request.POST)
#         self.object = self.get_object(queryset=Author.objects.all())
#         return super().post(request, *args, **kwargs)
    
#     def get_form(self, form_class=None):
#         return AuthorBooksFormset(instance=self.object, **self.get_form_kwargs())
        
    
#     def form_valid(self, form):
#         form.save()
#         return HttpResponseRedirect(self.get_success_url())
    
#     def get_success_url(self):
#         return reverse('books:author_detail', kwargs= {'pk':self.object.pk})

class AuthorBooksEdit(SingleObjectMixin, FormView):
    model = Author
    template_name = 'new_books/author_books_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'POST':
            kwargs.update({'data': self.request.POST, 'files': self.request.FILES})
        return kwargs

    def get_form(self, form_class=None):
        return AuthorBooksFormset(instance=self.object, **self.get_form_kwargs())

    def form_valid(self, form):
        print("Saving form...")
        instances = form.save( comm)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print("Form Errors:", form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('books:author_detail', kwargs={'pk': self.object.pk})

    