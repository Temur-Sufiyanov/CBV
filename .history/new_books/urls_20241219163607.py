from django.urls import path
from .views import (HomeView, AuthorView, Au)

app_name = 'books'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('author/', AuthorView.as_view(), name='authors'),
]
