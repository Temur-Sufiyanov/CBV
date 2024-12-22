from django.urls import path 
from .views import IndexView, BookDetail

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('book<slug:slug>/', BookDetail.as_view(), name='book-detail'),
]

