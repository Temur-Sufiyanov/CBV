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

from django.forms import modelformset_factory
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

class AuthorBooksEdit(SingleObjectMixin, FormView):
    model = Author
    template_name = 'new_books/author_books_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())  # Get the Author instance
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())  # Get the Author instance
        formset = AuthorBooksFormset(self.request.POST, instance=self.object)  # Bind data to the formset

        if formset.is_valid():
            formset.save()  # Save changes
            messages.success(self.request, "Changes were saved!")
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=formset))

    def get_form(self, form_class=None):
        # Create a new formset with the current Author instance
        return AuthorBooksFormset(instance=self.object, **self.get_form_kwargs())

    def get_success_url(self):
        return reverse('books:author_detail', kwargs={'pk': self.object.pk})
