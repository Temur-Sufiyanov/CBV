from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Book
# Create your views here.

class IndexView(TemplateView):
    
    template_name = 'book/home.html'
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['books'] = 
        return 

