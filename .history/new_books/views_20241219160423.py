from django.shortcuts import render
from django.views.generic import (TemplateView, ListView)
from .models import Aut
# Create your views here.

class HomeView(TemplateView):
    template_name = 'new_books/home.html'
    
class AuthorView(ListView):
    model = 