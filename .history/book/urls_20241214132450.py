from django.urls import path 
from .views import IndexView, BookDetail, GenreView, AddView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<slug:slug>/', BookDetail.as_view(), name='book-detail'),
    path('g/<str:genre>', GenreView.as_view(), name='genre'),
    path('add/', AddView.as_view(), name='new_book'),
]

