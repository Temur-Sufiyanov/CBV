from django.shortcuts import render, redirect
from django.contrib.auth.views import redirect_to_login
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .forms import AddForm
from .models import Book
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
# Create your views here.



class AccesUserMixin(PermissionRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.)
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
    
    # def get_queryset(self):
    #     return Book.objects.all()[:1]
    
class GenreView(ListView):
    model = Book
    template_name = 'book/home.html'
    context_object_name = reverse_lazy('home')
    
    def get_queryset(self, *args, **kwargs):
        return Book.objects.filter(genre__icontains = self.kwargs.get('genre'))


# class AddBookView(FormView):
#     form_class = AddForm
#     template_name = 'book/form.html'
#     success_url = 'home'
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
   
class AddBookView(CreateView):
    model = Book
    form_class = AddForm
    template_name = 'book/form.html'
    success_url = reverse_lazy('home')
   
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    
    permission_required = 'book.schange_book'
    permission_denied_message = ''
    login_url = reverse_lazy('home')  
    model = Book
    form_class = AddForm
    template_name = 'book/form.html'
    success_url = reverse_lazy('home')
    
class BookDetail(DetailView):
    
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'