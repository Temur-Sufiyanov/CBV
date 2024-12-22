from django.urls import path 
from .views import IndexView, BookDetail, GenreView, AddBookView, BookUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('add/', AddBookView.as_view(), name='new_book'),
    path('<slug:slug>/', BookDetail.as_view(), name='book-detail'),
    path('<slug:slug>/edit/', BookUpdateView.as_view()),
    path('g/<str:genre>/', GenreView.as_view(), name='genre'),
    
]

