from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import 
from .models import Book
# Create your views here.

class IndexView(TemplateView):
    
    template_name = 'book/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        
        return context

