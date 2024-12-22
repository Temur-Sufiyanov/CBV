from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import B
# Create your views here.

class IndexView(TemplateView):
    
    template_name = 'book/home.html'
