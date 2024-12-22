from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
# Create your views here.

# class IndexView(TemplateView):
    
#     template_name = 'book/home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = Book.objects.all()
        
#         return context

class IndexView(ListView):
    model = Book
    template_name = 'book/home.html'
    context_object_name = 'books'
    # paginate_by = 1
    # queryset = Book.objects.all()[:2]
    
    def get_queryset(self):
        return Book.objects.all()[:1]
    
class Genge

class BookDetail(DetailView):
    
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'